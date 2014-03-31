#!/bin/sh -e

PKG="powernap"
MAJOR=1

error() {
	echo "ERROR: $@"
	exit 1
}

head -n1 debian/changelog | grep "unreleased" || error "This version must be 'unreleased'"

./debian/rules get-orig-source
bzr bd
sed -i "s/) unreleased;/-0ubuntu1) karmic;/" debian/changelog
bzr bd --builder "debuild -S -sa" --source
minor=`head -n1 debian/changelog | sed "s/^.*($MAJOR.//" | sed "s/-.*$//"`
dch --release
debcommit --release
newminor=`expr $minor + 1`
dch -v "$MAJOR.$newminor" "UNRELEASED"
sed -i "s/$MAJOR.$newminor) .*;/$MAJOR.$newminor) unreleased;/" debian/changelog

gpg --armor --sign --detach-sig ../"$PKG"_*.orig.tar.gz

echo
echo
echo "To test:"
echo "  sudo dpkg -i ../*.deb"
echo
echo "To commit and push:"
echo "  bzr cdiff"
echo "  bzr commit -m 'releasing $MAJOR.$minor, opening $MAJOR.$newminor' && bzr push lp:$PKG"
echo
echo "Publish tarball at:"
echo "  https://launchpad.net/$PKG/trunk/+addrelease"
echo
echo
