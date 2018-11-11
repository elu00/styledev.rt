# styledev.rt
(HackPrinceton 2018) Game asset style transfer for easily extensible fan mods and creations.
## About
[Style Transfer](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf) is a relatively new subfield in machine learning that allows for the quantification of image "styles," typically thought of as "brush patterns" or other local geometry in an image. 
By training a neural network to quantify such styles, it's possible to "transfer" the style of one image onto another, creating a variety of interesting results, including ["Deep Fakes'](https://www.cmu.edu/news/stories/archives/2018/september/deep-fakes-video-content.html) and other forms of content.

However, while these algorithms have been adapted to [video content](https://www.youtube.com/watch?v=Khuj4ASldmU), including some working demos on [live video feeds](https://www.youtube.com/watch?v=vAelubuwquE), such techniques often remain computationally infeasible, requiring anywhere from seconds to minutes to process a single frame on typical hardware. 
In this project, we offer true real-time style transfer through pre-computed "style transferred" modified game asset, rendering such assets in real time with the original game engine.
## Screenshots
Base Style:
![Base Style](https://raw.githubusercontent.com/elu00/styledev.rt/master/demo/baseStyle.jpg)
![Screenshot 1](https://raw.githubusercontent.com/elu00/styledev.rt/master/demo/screenshots/Default1.png)
![Screenshot 2](https://raw.githubusercontent.com/elu00/styledev.rt/master/demo/screenshots/Default2.png)
![Screenshot 3](https://raw.githubusercontent.com/elu00/styledev.rt/master/demo/screenshots/Default3.png)
![Screenshot 4](https://raw.githubusercontent.com/elu00/styledev.rt/master/demo/screenshots/Default4.png)
## Demo
To run our modded first level of "Paper Mario: The Thousand Year Door":
- Install [Dolphin Emulator](https://dolphin-emu.org/)
- Clone this repo, and copy "demo/modded_textures" to "Your Documents Folder/Dolphin Emulator/Load/Textures"
- Under Dolphin/Graphics Settings/Advanced, tick "Load Custom Textures"
- Run TTYD from Dolphin
## Requirements
Running this project depends on the following packages (available through conda or pip) 
-  torch, torch.nn, numpy 
-  torch.optim
-  PIL, PIL.Image, 
-  torchvision.transforms
-  torchvision.models
## Usage
1. Tick "dump textures" under Dolphin/Graphics/Advanced. Then play through the desired level(s) that you wish to mod/style transfer onto.  
2. Run 
```
python run_this.py
```
in your terminal of choice. 
By default, this uses the textures listed in `demo/dumped_textures` to determine which textures to replace/style on, searching through all the files listed in `demo/base_textures` and replacing them in-place. The style to be used is computed from "demo/style.jpg." 
After doing this, follow the instructions for running the demo.
## Credits
Thanks to [The Dolphin Community TTYD Texture pack](https://forums.dolphin-emu.org/Thread-paper-mario-ttyd-hd-texture-pack-v1-7-july-4-2018), [Alexis Jacq et. al](https://pytorch.org/tutorials/advanced/neural_style_tutorial.html), and the Dolphin Team.
