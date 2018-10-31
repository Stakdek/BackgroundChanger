 #!/bin/bash
background_changer() {
    for dat in $HOME/Bilder/Wallpapers/*.png # your pics path
    do
        gsettings set org.gnome.desktop.background picture-uri "file:///$dat"
        gsettings set org.gnome.desktop.screensaver picture-uri "file:///$dat"
        echo $dat
        sleep 30 # 300 seconds as standard
    done

}

while true
      do
          background_changer
done
