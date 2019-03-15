 #!/bin/bash

rm -v ~/Library/Preferences/com.apple.spotsearching.plist

# Navicat
echo "reset Navicat..."
rm -v ~/Library/Application\ Support/PremiumSoft\ CyberTech/Navicat*/Navicat*/.tc*
rm -v ~/Library/Caches/com.prect.Navicat*/.tc*
rm -v ~/Library/Preferences/com.prect.NavicatPremium*.plist