import folium


iconUSR = folium.features.CustomIcon(icon_image='map-object-userGreen.png', icon_size=(50, 50))

icon = folium.features.CustomIcon(icon_image='imagesBus2.png', icon_size=(50, 50))
icon2 = folium.features.CustomIcon(icon_image='imagesBus2.png', icon_size=(50, 50))
icon3 = folium.features.CustomIcon(icon_image='imagesBus2.png', icon_size=(50, 50))
icon4 = folium.features.CustomIcon(icon_image='imagesBus2.png', icon_size=(50, 50))
icon5 = folium.features.CustomIcon(icon_image='imagesBus2.png', icon_size=(50, 50))

iconTR = folium.features.CustomIcon(icon_image='imagesTRAM1.png', icon_size=(50, 50))
iconTR2 = folium.features.CustomIcon(icon_image='imagesTRAM1.png', icon_size=(50, 50))
iconTR3 = folium.features.CustomIcon(icon_image='imagesTRAM1.png', icon_size=(50, 50))
iconTR4 = folium.features.CustomIcon(icon_image='imagesTRAM1.png', icon_size=(50, 50))
iconTR5 = folium.features.CustomIcon(icon_image='imagesTRAM1.png', icon_size=(50, 50))

icont = folium.features.CustomIcon(icon_image='train-metropolitan.png', icon_size=(50, 50))
icont2 = folium.features.CustomIcon(icon_image='train-metropolitan.png', icon_size=(50, 50))
icont3 = folium.features.CustomIcon(icon_image='train-metropolitan.png', icon_size=(50, 50))
icont4 = folium.features.CustomIcon(icon_image='train-metropolitan.png', icon_size=(50, 50))
icont5 = folium.features.CustomIcon(icon_image='train-metropolitan.png', icon_size=(50, 50))



coords = (44.9236189, 4.8879461)
map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=15)

coords = [44.931521, 4.890457]
folium.Marker(location=coords, popup="USR", icon=iconUSR).add_to(map)

coords = [44.931254, 4.889557]
folium.Marker(location=coords, popup="CITEA", icon=icon).add_to(map)
coords = [44.930532, 4.890241]
folium.Marker(location=coords, popup="CITEA", icon=icon2).add_to(map)
coords = [44.932128,  4.8887]
folium.Marker(location=coords, popup="CITEA", icon=icon3).add_to(map)
coords = [44.935024,  4.892084]
folium.Marker(location=coords, popup="CITEA", icon=icon4).add_to(map)
coords = [44.933787 ,  4.891894]
folium.Marker(location=coords, popup="CITEA", icon=icon5).add_to(map)


coords = [44.932226,   4.889942]
folium.Marker(location=coords, popup="TRAIN'RETARD", icon=icont).add_to(map)
coords = [44.931139,   4.88963]
folium.Marker(location=coords, popup="TRAIN'RETARD", icon=icont2).add_to(map)
coords = [44.933289 ,  4.889019]
folium.Marker(location=coords, popup="TRAIN'RETARD", icon=icont3).add_to(map)
coords = [44.933464 ,  4.890403]
folium.Marker(location=coords, popup="TRAIN'RETARD", icon=icont4).add_to(map)
coords = [44.933274,  4.891744]
folium.Marker(location=coords, popup="TRAIN'RETARD", icon=icont5).add_to(map)

coords = [44.932507,  4.886026]
folium.Marker(location=coords, popup="TRAM'PAVITE", icon=iconTR).add_to(map)
coords = [44.93119 ,  4.888916]
folium.Marker(location=coords, popup="TRAM'PAVITE", icon=iconTR2).add_to(map)
coords = [44.931349,  4.892639]
folium.Marker(location=coords, popup="TRAM'PAVITE", icon=iconTR3).add_to(map)
coords = [44.930096 ,  4.889624]
folium.Marker(location=coords, popup="TRAM'PAVITE", icon=iconTR4).add_to(map)
coords = [44.935656,  4.893508]
folium.Marker(location=coords, popup="TRAM'PAVITE", icon=iconTR5).add_to(map)


map.save(outfile='map.html')

