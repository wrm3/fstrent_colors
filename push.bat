git status  # Check what needs to be committed
git add .
git commit -m "Ready for release"

# For bug fixes (0.1.3 -> 0.1.4):
bump2version patch
# For new features (0.1.3 -> 0.2.0):
# bump2version minor
# For breaking changes (0.1.3 -> 1.0.0):
# bump2version major

git push origin main
git push --tags
