# SVMod

A simple tool to copy files to and from your Shadowverse installation on Windows.

## Usage

How to use this tool to install Shadowverse mods:

1. Download the executable.
2. Create a folder named "Mods" in the same location as the execuable.
3. Download and extract mods into the "Mods" folder. (Each mod should be a folder that contains a "mod.json" file; make sure you aren't extracting a folder containing the mod.)
4. If using a mod that requires files from the Japanese version of the game (e.g. iDOLM@STER emblems/sleeves mod):
	1. Change the game language to Japanese from Steam's properties window.
	2. Start the game to download data. (Not 100% sure this is necessary.)
	3. Run the executable and use the first option to copy files from the Shadowverse installation to the respective mods' folders.
	4. Change the game language back to English.
	5. Start the game to download data. (Again, not sure this is necessary.)
5. Run the executable and use the second option to copy the modded files to your Shadowverse installation.

## Mods

A description of the file format for mods.

### mod.json

A mod should be a folder with a "mod.json" file, which should include metadata for the mod in json format. The currently defined keys are:

| Key         | Description |
| ----------- | ----------- |
| name        | The name of the mod |
| description | A description of the mod |
| author      | The author, in the format "Name (URL)" |
| version     | A version number string for the mod |
| copy_files  | An object specifying files to copy from the Japanese version of the game. Each key should be the name of a folder in the Shadowverse installation (or "." for the root), and each value should be an array of names of files to copy.<br><br>_(Most mods won't need this functionality; this primarily exists for the IM@S mod since the emblems/sleeves files change frequently. The Isabelle mod can be updated with this as well, but those files don't change nearly as often.)_ |

### Other files

External files to copy into the Shadowverse installation should be in a subdirectory named "Files". (This is probably how most mods will include their mod files.)

Here's an example mod directory tree:

```
mod folder
├─mod.json
└─Files
  ├─a
  │ ├─foo.unity3d
  │ └─bar.unity3d
  └─v
    └─something.acb
```

Note: The "mod.json" file isn't strictly necessary right now for mods that don't use copy_files (i.e. most mods), since the other metadata aren't used anywhere, but it's good information to have, and it might be used in the future to display and select individual mods to install.

## Disclaimer

Modifying and distributing game files is against the [Shadowverse Terms of Service](https://shadowverse.com/terms.php) (Article 5.3). The creator of this tool is not responsible for anything that happens to users or their accounts as a result of using this tool.

(end disclaimer)<br>
That being said, I don't think Cygames has much reason to go around suspending accounts or anything just for modifying art in local game files.
