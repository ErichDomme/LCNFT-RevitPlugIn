<h1 align="center">
  <a name="logo"><img src="img\icon_nft.svg" alt="UMNFT" width="300"></a>
  <br>
  Urban Mining NFT <br>
  - UMNFT - <br>
  Revit PlugIn
</h1>

<div align="center"></div>

<p><font size="3">
This project was developed during my Master Thesis at RWTH Aachen University. This Extension is one . </p>

## General Information
.


## Requirements
> It is assumed that you have Autodesk Revit installed on your computer!<br>
> Revit 2023 has been used for development!<br>
> Except for pyRevit, the other requirements are not mandatory! But they might be, as I will be looking at the extensions in the future!<br>

__Revit Requirements__
1. [__pyRevit__](https://github.com/eirannejad/pyRevit/releases/tag/v4.8.12.22247%2B0031)
2. [RevitPythonShell](https://github.com/architecture-building-systems/revitpythonshell)
3. [RevitLookup](https://github.com/jeremytammik/RevitLookup)
4. [Revitron](https://github.com/revitron/revitron)
5. [Revitron-UI](https://github.com/revitron/revitron-ui)
6. [Speckle](https://speckle.systems/)

## Installation
In order for UMNFT to run on your computer, you will need to do a few installations beforehand. UMNFT is based on pyRevit and this is where we start.
1. Make sure you have Autodesk Revit installed on your computer!
2. Install the latest [pyRevit version](https://github.com/eirannejad/pyRevit/releases), during the development of Cross-Tools the version [v4.8.13.23182](https://github.com/eirannejad/pyRevit/releases/tag/v4.8.13.23182%2B2215) was used. The installation is self-explanatory and very well documented, but a look at the [Notion Page](https://pyrevitlabs.notion.site/pyrevitlabs/pyRevit-bd907d6292ed4ce997c46e84b6ef67a0) is worthwhile.
3. After the successful installation of pyRevit, Navigate now to the extensions of pyRevit, under the first tab. 
<div align="center">
<img src="./img/Pyrevit_Extensions.png" >
</div>

4. You should now see a list of all extensions that are either written by pyRevit itself or recommended by pyRevit, this is the __pyRevit Extension Manager__. We now want to add "UMNFT" to this list!
> __"UMNFT" should not be visible to you yet, as shown in the screenshot below!__<br>

<div align="center">
<img src="./img/Pyrevit_Extension_Manager_Step01.png" >
</div>


5. To do this, we need to find the location of these listed extensions. They are written inside a json file, with the name "extensions.json"! This should be found here:<br>
`C:\Users\cxs-user\AppData\Roaming\pyRevit-Master\extensions\`

6. Add the following code snippet at the end of the json file:
> :warning: **You will need admin rights here!** Be very careful! If in doubt, contact your IT support!
````
        {
            "builtin": "False",
            "default_enabled": "True",
            "type": "extension",
            "rocket_mode_compatible": "False",
            "name": "cross",
            "description": "Extensions for Cross Architecture",
            "author": "Erich Domme",
            "author_profile": "https://github.com/CrossArchitecture",
            "url": "https://github.com/CrossArchitecture/cross.git",
            "website": "https://github.com/CrossArchitecture",
            "image": "",
            "dependencies": []
        }
````
> __Make sure you place the commas in the right place!__
````
{
    "extensions": [
        {
            n. Extension
        },
        {
            cross
        }
    ]
}
````

7. Depending on your system it may be enough to reload pyRevit __and__ update it once. However, my recommendation would be a __restart__ of Revit. Any changes will be added automatically. 

8. Navigate to the __pyRevit Extension Manager__ again. You should now be able to see "cross"!

<div align="center">
<img src="./img/Pyrevit_Extension_Manager_Step02.png" >
</div>

9. "Cross-Tools" is currently not a private repository. But that can change, therefore the check box "Git repository is private" has not to be checked! If you want to get the access token, after it is private, contact [me](mailto:erich.domme@rwth-aachen.de)!

<div align="center">
<img src="./img/Pyrevit_Extension_Manager_Step03.png" >
</div>

10. In contrast to me, "cross" will not yet be installed in your Revit. You should do this by clicking on Install Extension.

<div align="center">
<img src="./img/Pyrevit_Extension_Manager_Step04.png" >
</div>

11. Done! You should now have "cross" in Revit!

<p align="center">
  <img src=https://media3.giphy.com/media/rY93u9tQbybks/giphy.gif?cid=ecf05e47eap1wzrxxzfedemp62jtrogwbslh12q694q9hdef&ep=v1_gifs_related&rid=giphy.gif&ct=g.gif alt="animated" />
</p>
<p align="center"><font size="3">
Congratulations!</p>


## Cross Tools - Features

<div align="center">
<img src="./img/Toolbar.png" >
<p>The "cross" Extension visible in the Revit toolbar</p>
</div>

<details>
<summary>Dimension</summary>
Dimension Line based Elements [Python]<br>
</details>

<details>
<summary>Generate</summary>
Beam(s) through input Surface [Dynamo]<br>
</details>

<details>
<summary>Parameter</summary>
Disallow Join [Python]<br>
Wall constraints: Base [Python]<br>
Wall constraints: Base & Top [Python]<br>
Wall constraints: Top [Python]<br>
</details>

<details>
<summary>Room Book</summary>
01 Generate Parameter [Dynamo]<br>
02 Assign Doors and Windows to their Rooms [Dynamo]<br>
03 Assign Finished and Raw Room Height [Dynamo]<br>
04 Assign Elevation Height [Dynamo]<br>
</details>

<details>
<summary>Selection</summary>
Same category as selected [Python]<br>
Same type as selected [Python]<br>
Titleblocks on sheets [Python]<br>
Select only of categories [Python]<br>
Select only 3D [Python]<br>
Select only 2D [Python]<br>
Deselect grouped elements [Python]<br>
Isolate Panels [Dynamo]<br>
</details>

<details>
<summary>Sheets</summary>
Place View(s) on Sheet [Dynamo]<br>
</details>

<details>
<summary>Tag</summary>
Center Room Tags [Python]<br>
</details>

<details>
<summary>Warning</summary>
Warning Management [Dynamo]<br>
Reset Graphical Override [Dynamo]<br>
</details>

<details>
<summary>Purge</summary>
Purge Delete Backups [Python]<br>
Purge DWG Line Patterns [Python]<br>
Purge imported dwg [Python]<br>
Purge unused scope boxes [Python]<br>
Purge unplaced views [Python]<br>
Purge unused sheets [Python]<br>
Remove unplaced rooms [Python]<br>
Remove unplaced areas [Python]<br>
Remove unenclosed areas [Python]<br>
Delete Family [Python]<br>
Delete selected unplaced Views [Dynamo]<br>
Delete unused View Template [Dynamo]<br>
Delete unused Filters [Dynamo]<br>
Ungroup all [Python]<br>
</details>

<details>
<summary>Excel</summary>
Excel [Dynamo]<br>
</details>

<details>
<summary>Testing</summary>
Testing Dynamo [Dynamo]<br>
Testing Python [Python]<br>
</details> 


## Screenshots


## Usage



## Project Status
<span style="color:green">**Version 0.0.1 published!**</span>
<!-- _complete_ / _no longer being worked on_. If you are no longer working on it, provide reasons why.-->


## Room for Improvement
Room for improvement:
- Improvement to be done
- More Room Book Tools for stepwise creation

To do:
- Dimension Tool is still work in progress


## Acknowledgements
Without these people and their projects, Cross-Tools would not have been possible:
- [Ehsan Iran-Nejad](https://github.com/eirannejad) with [pyRevit](https://github.com/eirannejad/pyRevit)
- [Erik Frits](https://github.com/ErikFrits) with [EF-Tools](https://github.com/ErikFrits/EF-Tools)
- [Gavin Crump, aussieBIMguru](https://github.com/aussieBIMguru) with [guRoo](https://github.com/aussieBIMguru/guRoo/tree/main/guRoo.tab/Tools.panel)
- [Marc Anton Dahmen](https://github.com/marcantondahmen) with [revitron](https://github.com/revitron/revitron)
- [Jean-Marc Couffin](https://github.com/jmcouffin) with [bimone](https://github.com/bimone/scripts-dynamo)


## Contact
Created by [Erich Domme](mailto:erich.domme@rwth-aachen.de) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->