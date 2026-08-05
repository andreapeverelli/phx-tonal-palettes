pkgname=phx-tonal-palette
pkgver=1.0.2
pkgrel=1
pkgdesc="sRGB/Display P3/Rec 2020 tonal palette based on Material You tones in HCT space"
arch=('any')
url="https://github.com/andreapeverelli/phx-tonal-palette.git"
license=('GPL-3.0')

depends=(
	'python'
	'python-pip'
)

build() {
	python -m venv ../.venv/phx-tonal-palette/
	source ../.venv/phx-tonal-palette/bin/activate
	pip install coloraide nuitka
	python -m nuitka --onefile --standalone --output-filename=../bin/phx-tonal-palette main.py
}

package() {
	install -dm755 "$pkgdir/usr/share/$pkgname"
	cp ../LICENSE $pkgdir/usr/share/$pkgname
	install -Dm755 ../bin/phx-tonal-palette $pkgdir/usr/bin/phx-tonal-palette
}
