import unreal
import os
import json
import shutil

### Setup paths here ###

sequencer_asset_path = '/Game/Cinematics/Master.Master'
output_folder = 'Y:/VFXTricks/Projects/0_Test/sequencer_export'

### End of setup ###

### Set export options ###
json_file = os.path.join(output_folder, 'shots_data.json')

export_options = unreal.FbxExportOption()
export_options.ascii = False
export_options.level_of_detail = False
export_options.collision = False
export_options.vertex_color = False
export_options.fbx_export_compatibility = unreal.FbxExportCompatibility.FBX_2020

world = unreal.EditorLevelLibrary.get_editor_world()

master_sequence = unreal.load_asset(sequencer_asset_path, unreal.LevelSequence)
tracks = master_sequence.get_master_tracks()
sections = tracks[0].get_sections()

shots_data = []

# create or clear output folder
if os.path.isdir(output_folder):
    shutil.rmtree(output_folder)
    os.makedirs(output_folder)
else:
    os.makedirs(output_folder)

# write shot json data
for section in sections:
    shot = section.get_shot_display_name()
    shot = shot.split('_')[0]
    output_file = os.path.join(output_folder, shot + '.fbx')
    section_start = section.get_start_frame()
    section_end = section.get_end_frame()
    section_length = section_end - section_start
    sequence = section.get_editor_property('sub_sequence')
    bindings = sequence.get_bindings()
    unreal.SequencerTools.export_fbx(world, sequence, bindings, export_options, output_file)
    start = sequence.get_playback_start()
    end = sequence.get_playback_end()
    data = {
        'shot': shot,
        'start': start,
        'end': start + section_length,
    }
    shots_data.append(data)

with open(json_file, 'w') as file:
    json.dump(shots_data, file)
