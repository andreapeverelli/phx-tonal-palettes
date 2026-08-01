import sys
import json
from coloraide import Color as Base
from coloraide.spaces.hct import HCT
from coloraide.distance.delta_e_hct import DEHCT
from coloraide.gamut.fit_hct_chroma import HCTChroma

if sys.argv[1] == "--version":
    sys.stdout.write("PHX-TONAL-PALETTE v1.0.1\n")
    sys.exit(0)

if sys.argv[1] == "--help":
    sys.stdout.write("PHX-TONAL-PALETTE\n\nCommand structure:\n | phx-tonal-palette hct_hue hct_chroma\n | phx-tonal-palette --version\n | phx-tonal-palette --help\n")
    sys.exit(0)

class Color(Base): ...

Color.register([HCT(), DEHCT(), HCTChroma()])

color = Color("hct", [sys.argv[1], sys.argv[2], 50])
tones = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 98, 99, 100]

palette = {
        "srgb": [color.clone().set("tone", tone).convert("srgb").to_string(hex=True, fit={"method": "hct-chroma", "jnd": 0.0}) for tone in tones],
    "display_p3": [color.clone().set("tone", tone).convert("display-p3").fit(method= "hct-chroma", jnd= 0.0).to_dict() for tone in tones],
    "rec_2020": [color.clone().set("tone", tone).convert("rec2020").fit(method= "hct-chroma", jnd= 0.0).to_dict() for tone in tones],
}

json.dump(palette, sys.stdout)
sys.exit(0)
