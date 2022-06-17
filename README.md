<img src="https://user-images.githubusercontent.com/9046931/172205434-25c8b7d1-816c-4689-935d-7717d00e27ab.svg" width="500">


# VFX Tricks Toolbox - [www.vfxtricks.com](http://www.vfxtricks.com)


Contents:
- [Houdini HDAs and Shelftools](https://github.com/VFX-Tricks/VFX-Tricks-Toolbox#1-houdini-hdas-and-shelftools)
- [Deadline plugins](https://github.com/VFX-Tricks/VFX-Tricks-Toolbox#2-deadline-plugins)
- [Unreal Engine Sequencer Exporter](https://github.com/VFX-Tricks/VFX-Tricks-Toolbox#3-unreal-engine-sequencer-exporter)

See [Installation guide](VFXTricksToolbox_install_guide_en.pdf)

Submit bugs and feature requests via [Issues](https://github.com/VFX-Tricks/VFX-Tricks-Toolbox/issues)

Feedback is welcome via [Discussions](https://github.com/VFX-Tricks/VFX-Tricks-Toolbox/discussions)

# 1. Houdini HDAs and Shelftools
https://www.sidefx.com/

The main goal of Houdini tools is to accelerate content creation at VFX Tricks. Creating setups and tutorials is time consuming. Mundane tasks like caching, publishing and farm submission shouldn't be a slowing down factor. Writing and reading caches is at the heart of every VFX pipeline 🎥, it needs to be quick, easy and reliable. After seeing many implementations at various studios, I decided to make my own that will suit VFX Tricks creators needs. This package will include caching and setup/shot specific tools.

⚠️ HDAs are in Indie .hdalc format


## Cacher SOP
<img src="https://user-images.githubusercontent.com/9046931/172088904-22ed52f4-7f09-4ddb-8579-5dd55f0c9bdd.png" width="500">

- .usd, .bgeo.sc and .vdb
- USD geometry purpose (render, proxy and guide)
- version control and stats 📝
- sections (wedging) 🍕

## Lop Cacher Import
<img src="https://user-images.githubusercontent.com/9046931/172474865-c958043b-d963-497d-9a5f-09eb4a7456ef.png" width="500">

- dynamically import .usd Cachers to LOP network
- well suited for Multishot workflow

## Multishot workflow
<img src="https://user-images.githubusercontent.com/9046931/172475669-c3385945-612e-4e4f-8021-e5b64bfa4b3e.png" width="500">

At VFX Tricks we usually provide single hip file with multiple shots inside. For single artist working on mulitple shots, I find this way better than conventional approach at VFX studios(each shot/element in separate hip file).

## Shelftools
<img src="https://user-images.githubusercontent.com/9046931/172474004-f87f45f2-862f-4a3a-80fb-f877a46caf1e.png" width="500">

- create OBJ contexts for each shot
- import shots from UE Sequencer
- set frame range per shot
- toggle cooking mode - I recommend assigning a hotkey -> must have!
- Cacher SOP and Farm Submiter ROP take advantage of this workflow

# 2. Deadline plugins
https://www.awsthinkbox.com/deadline <br>
https://docs.thinkboxsoftware.com/products/deadline/10.1/1_User%20Manual/manual/app-index.html

VFX Tricks Toolbox extends existing Houdini plugins shipped with Deadline.

- USD caching - SOP and Stage
- USD rendering via command line utility - [husk](https://www.sidefx.com/docs/houdini/ref/utils/husk.html)
- sections(wedges) submits hip file only once. Current section(wedge) is defined by env variable, resulting faster submission to farm ⏱

<img src="https://user-images.githubusercontent.com/9046931/172478881-4d28afcf-d6ba-479d-b2f0-44ded527fdb9.png" width="500">

# 3. Unreal Engine Sequencer Exporter
https://docs.unrealengine.com/5.0/en-US/unreal-engine-sequencer-movie-tool-overview/

A quick way of exporting animated assets (static mesh, camera, etc.) from Sequencer to FBX with supporting JSON data file. <br>
Then import to Houdini each shot as a Multishot context with corresponding assets and frame ranges.

<img src="https://user-images.githubusercontent.com/9046931/172036894-9816bc65-295e-4f32-974a-8148c01ccc5d.jpg" width="500">



