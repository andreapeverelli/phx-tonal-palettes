import sys
import json
from coloraide import Color as Base
from coloraide.spaces.hct import HCT
from coloraide.distance.delta_e_hct import DEHCT
from coloraide.gamut.fit_hct_chroma import HCTChroma

def badArguments():
    sys.stdout.write("""\
Bad arguments.
Try 'phx-tonal-palette --help' for command structure.
""")
    sys.exit(1)

if len(sys.argv) < 2:
    badArguments()

if sys.argv[1] == "--version":
    sys.stdout.write("PHX-TONAL-PALETTE v1.0.3\n")
    sys.exit(0)

if sys.argv[1] == "--help":
    sys.stdout.write("""\
PHX-TONAL-PALETTE
sRGB/Display P3/Rec 2020 tonal palette based on Material You tones in HCT space.

Command structure:
    phx-tonal-palette HCT_HUE HCT_CHROMA
    phx-tonal-palette --version
    phx-tonal-palette --help
""")
    sys.exit(0)

if len(sys.argv) < 3:
    badArguments()

class Color(Base): ...

Color.register([HCT(), DEHCT(), HCTChroma()])

color = Color("hct", [sys.argv[1], sys.argv[2], 50])
tones = [0, 4, 6, 10, 12, 17, 20, 22, 24, 30, 40, 50, 60, 70, 80, 87, 90, 92, 94, 95, 96, 98, 99, 100]

palette = {
        "srgb": [color.clone().set("tone", tone).convert("srgb").to_string(hex=True, fit={"method": "hct-chroma", "jnd": 0.0}) for tone in tones],
    "display-p3": [color.clone().set("tone", tone).convert("display-p3").fit(method= "hct-chroma", jnd= 0.0).to_dict() for tone in tones],
    "rec2020": [color.clone().set("tone", tone).convert("rec2020").fit(method= "hct-chroma", jnd= 0.0).to_dict() for tone in tones],
    "hct": [color.clone().set("tone", tone).fit(method= "hct-chroma", jnd= 0.0).to_dict() for tone in tones],
}

json.dump(palette, sys.stdout)
sys.exit(0)
