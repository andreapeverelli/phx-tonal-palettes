import sys
import json
from coloraide import Color as Base
from coloraide.spaces.hct import HCT
from coloraide.distance.delta_e_hct import DEHCT
from coloraide.gamut.fit_hct_chroma import HCTChroma

if len(sys.argv) > 1:
    if sys.argv[1] == "--version":
        sys.stdout.write("PHX-TONAL-PALETTES v2.0.0\n")
        sys.exit(0)

    if sys.argv[1] == "--help":
        sys.stdout.write("""\
PHX-TONAL-PALETTES
sRGB/Display P3/Rec 2020 tonal palettes based on Material You tones in HCT space.

Command structure:
    phx-tonal-palette < BASE_COLORS_JSON
    phx-tonal-palette --version
    phx-tonal-palette --help

BASE_COLORS_JSON structure:
{
    "BASE_COLOR_NAME": {
        "hue": BASE_COLOR_HUE_FLOAT,
        "chroma": BASE_COLOR_CHROMA_FLOAT
    }
}
""")
        sys.exit(0)

class Color(Base): ...

Color.register([HCT(), DEHCT(), HCTChroma()])

colors = json.load(sys.stdin)
tones = [0, 4, 6, 10, 12, 17, 20, 22, 24, 30, 40, 50, 60, 70, 80, 87, 90, 92, 94, 95, 96, 98, 99, 100]

palette = {}
for base_color, hct_value in colors.items():
    color = Color("hct", [hct_value["hue"], hct_value["chroma"], 50])
    palette[base_color] = []

    for tone in tones:
        palette[base_color].append({
            "srgb":
                color
                    .clone()
                    .set("tone", tone)
                    .convert("srgb")
                    .to_string(hex=True, fit={"method": "hct-chroma", "jnd": 0.0}),
            "display-p3":
                color
                    .clone()
                    .set("tone", tone)
                    .convert("display-p3")
                    .fit(method= "hct-chroma", jnd= 0.0)
                    .to_dict()["coords"],
            "rec2020":
                color
                    .clone()
                    .set("tone", tone)
                    .convert("rec2020")
                    .fit(method= "hct-chroma", jnd= 0.0)
                    .to_dict()["coords"],
            "hct":
                color
                    .clone()
                    .set("tone", tone)
                    .to_dict()["coords"],
        })

json.dump(palette, sys.stdout)
sys.exit(0)
