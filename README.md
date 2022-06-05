<img src="https://user-images.githubusercontent.com/9046931/172026803-81ad8335-fa79-42b7-989d-2fd32e1f2168.svg" width="500">

# VFX Tricks Toolbox

Contents:
- [Houdini HDAs and Shelftools](https://github.com/VFX-Tricks/VFX-Tricks-Toolbox/blob/main/README.md#1-houdini-hdas-and-shelftools)
- [Deadline plugins](https://github.com/VFX-Tricks/VFX-Tricks-Toolbox/blob/main/README.md#2-deadline-plugins)
- [Unreal Engine Sequencer Exporter](https://github.com/VFX-Tricks/VFX-Tricks-Toolbox/blob/main/README.md#3-unreal-engine-sequencer-exporter)

See [Installation guide](VFXTricksToolbox_install_guide_en.pdf)

# 1. Houdini HDAs and Shelftools
https://www.sidefx.com/

The main goal of Houdini tools is to provide efficient caching workflows. Writing and reading caches is at the heart of every VFX pipeline 🎞️.

### Cacher main features
- .usd, .bgeo.sc and .vdb
- USD geometry purpose (render, proxy and guide)
- version control and stats 📝
- sections (wedging) 🍕

### Multishot workflow
At VFX Tricks usually we provide single hip file with multiple shots inside. For single artist working on mulitple shots, I find this way better than conventional approach at VFX studios(each shot/element in separate hip file).

Shelftools provide:
- define OBJ contexts for each shot
- set frame range per shot
- Cacher SOP and Farm Submiter ROP take advantage of this workflow

# 2. Deadline plugins
https://www.awsthinkbox.com/deadline <br>
https://docs.thinkboxsoftware.com/products/deadline/10.1/1_User%20Manual/manual/app-index.html

VFX Tricks Toolbox extends existing Houdini plugins shipped with Deadline.

- USD caching - SOP and Stage
- USD rendering via command line utility - [husk](https://www.sidefx.com/docs/houdini/ref/utils/husk.html)
- sections(wedges) submits hip file only once. Current section(wedge) is defined by env variable, resulting faster submission to farm ⏱️.

# 3. Unreal Engine Sequencer Exporter
https://docs.unrealengine.com/5.0/en-US/unreal-engine-sequencer-movie-tool-overview/

A quick way of exporting animated assets (static mesh, camera, etc.) from Sequencer to FBX with supporting JSON data file. <br>
Then import to Houdini each shot as a Multishot context with corresponding assets and frame ranges.

![sequencer_gh](https://user-images.githubusercontent.com/9046931/172036894-9816bc65-295e-4f32-974a-8148c01ccc5d.jpg)



