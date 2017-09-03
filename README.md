# SVMod

A tool to copy files to and from your Shadowverse installation on Windows.

## Usage

How to use this tool to install Shadowverse mods:

1. Download the executable.
2. Create a folder named "Mods" in the same location as the execuable.
3. Download and extract mods into the "Mods" folder. (Each mod should be a folder that contains a "mod.json" file; make sure you aren't extracting a folder containing the mod.)
4. If using a mod that requires files from the Japanese version of the game (i.e. the iDOLM@STER emblems/sleeves mod), use the tool to copy files from the Japanese version (see the next subsection); otherwise, skip this step.
5. Run the executable and use the second option. This will copy the modded files to your Shadowverse installation.

Note: The order in which mods are applied is not set, so if multiple mods alter the same file, it's best to keep only the desired version of the file and to remove all other versions from their mod folders.

### Copying files from the Japanese version of the game

This is only necessary for mods like the iDOLM@STER emblems/sleeves mod that require files from the Japanese version of the game. Most mods will not require you to do this.

1. Change the game language to Japanese from Steam's properties window.
2. Start the game to download data. (Not 100% sure this is necessary.)
3. Run the executable and use the first option. This will copy files from the Shadowverse installation to the respective mods' folders.
4. Change the game language back to English.
5. Start the game to download data. (Again, not sure this is necessary.)

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
| copy\_files  | An object specifying files to copy from the Japanese version of the game. Each key should be the name of a folder in the Shadowverse installation (or "." for the root), and each value should be an array of names of files to copy.<br><br>_(Most mods won't need this functionality; this primarily exists for the IM@S mod since the emblems/sleeves files change frequently. The Isabelle mod can be updated using this as well, but those files don't change nearly as often.)_ |

Note: The "mod.json" file isn't strictly necessary right now for mods that don't use copy_files (i.e. most mods), since the other metadata aren't used anywhere, but it's good information to have, and it might be used in the future to display and select individual mods to install.

### Other files

External files to copy into the Shadowverse installation should be in a subdirectory named "Files". (This is probably how most mods will include their mod files.)

Here's an example mod directory tree:

```
mod folder
├─Files
│ ├─a
│ │ ├─foo.unity3d
│ │ └─bar.unity3d
│ └─v
│   └─something.acb
└─mod.json
```

### Packaging

When zipping mods to distribute them, please zip the files/folders inside the mod (i.e. "mod.json" and "Files"), and not the mod folder itself. There are plans to support zipped mods, and the possibility of having an extra folder inside the .zip file with an arbitrary name makes things a little annoying.

## Disclaimer

Modifying and distributing game files is against the [Shadowverse Terms of Service](https://shadowverse.com/terms.php) (Article 5.3). The creator of this tool is not responsible for anything that happens to users or their accounts as a result of using this tool.

(end disclaimer)<br>
That being said, it's unlikely that Cygames will go around suspending or banning accounts just for modifying art in local game files.
