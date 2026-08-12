pkgname=phx-tonal-palettes
pkgver=2.0.0
pkgrel=1
pkgdesc="sRGB/Display P3/Rec 2020 tonal palettes based on Material You tones in HCT space."
arch=("x86_64")
url="https://github.com/andreapeverelli/phx-tonal-palettes.git"
license=("GPL-3.0")

makedepends=(
	"python"
	"python-pip"
)

options=(!debug)

build() {
	mkdir -p ../bin
	mkdir -p ../.venv/phx-tonal-palettes
	python -m venv ../.venv/phx-tonal-palettes/
	source ../.venv/phx-tonal-palettes/bin/activate
	pip install coloraide nuitka
	python -m nuitka --onefile --standalone --output-filename=../bin/phx-tonal-palettes main.py
}

package() {
	install -dm755 "$pkgdir/usr/share/$pkgname"
	cp ../LICENSE $pkgdir/usr/share/$pkgname
	install -Dm755 ../bin/phx-tonal-palettes $pkgdir/usr/bin/phx-tonal-palettes
}
