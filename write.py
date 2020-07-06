import json

rx5700xt = {
    "MSI Radeon RX 5700 XT 8 GB GAMING X Video Card": "https://pcpartpicker.com/product/jbK2FT/msi-radeon-rx-5700-xt-8-gb-gaming-x-video-card-radeon-rx-5700-xt-gaming-x",
    "Sapphire Radeon RX 5700 XT 8 GB NITRO+ Video Card": "https://pcpartpicker.com/product/WGLwrH/sapphire-radeon-rx-5700-xt-8-gb-nitro-video-card-11293-03-40g",
    "PowerColor Radeon RX 5700 XT 8 GB Red Devil Video Card": "https://pcpartpicker.com/product/vK4BD3/powercolor-radeon-rx-5700-xt-8-gb-red-devil-video-card-axrx-5700xt-8gbd6-3dheoc",
    "XFX Radeon RX 5700 XT 8 GB THICC III Ultra Video Card": "https://pcpartpicker.com/product/qzPgXL/xfx-radeon-rx-5700-xt-8-gb-thicc-iii-ultra-video-card-rx-57xt8tbd8",
    "ASRock Radeon RX 5700 XT 8 GB Phantom Gaming D OC Video Card": "https://pcpartpicker.com/product/Vh9tt6/asrock-radeon-rx-5700-xt-8-gb-phantom-gaming-d-oc-video-card-rx5700xt-pgd-8go",
    "Gigabyte Radeon RX 5700 XT 8 GB GAMING OC Video Card": "https://pcpartpicker.com/product/6kdrxr/gigabyte-radeon-rx-5700-xt-8-gb-gaming-oc-video-card-gv-r57xtgaming-oc-8gd"

}

gtx1660s = {
    "Gigabyte GeForce GTX 1660 SUPER 6 GB OC Video Card": "https://pcpartpicker.com/product/CnpmP6/gigabyte-geforce-gtx-1660-super-6-gb-oc-video-card-gv-n166soc-6gd",
    "Gigabyte GeForce GTX 1660 SUPER 6 GB GAMING OC Video Card": "https://pcpartpicker.com/product/DdbCmG/gigabyte-geforce-gtx-1660-super-6-gb-gaming-oc-video-card-gv-n166sgaming-oc-6gd",
    "Zotac GeForce GTX 1660 SUPER 6 GB GAMING AMP Video Card": "https://pcpartpicker.com/product/sFZzK8/zotac-geforce-gtx-1660-super-6-gb-gaming-amp-video-card-zt-t16620d-10m",
    "EVGA GeForce GTX 1660 SUPER 6 GB SC ULTRA GAMING Video Card": "https://pcpartpicker.com/product/GzPgXL/evga-geforce-gtx-1660-super-6-gb-sc-ultra-gaming-video-card-06g-p4-1068-kr",
    "MSI GeForce GTX 1660 SUPER 6 GB VENTUS XS OC Video Card": "https://pcpartpicker.com/product/Z3wkcf/msi-geforce-gtx-1660-super-6-gb-ventus-xs-oc-video-card-gtx-1660-super-ventus-xs-oc"
}

rx5700 = {
    "Gigabyte Radeon RX 5700 8 GB GAMING OC": "https://pcpartpicker.com/product/hCbCmG/gigabyte-radeon-rx-5700-8-gb-gaming-oc-video-card-gv-r57gaming-oc-8gd",
    "MSI Radeon RX 5700 8 GB GAMING X": "https://pcpartpicker.com/product/nd9tt6/msi-radeon-rx-5700-8-gb-gaming-x-video-card-radeon-rx-5700-gaming-x",
    "PowerColor Radeon RX 5700 8 GB Red Devil": "https://pcpartpicker.com/product/vP3mP6/powercolor-radeon-rx-5700-8-gb-red-devil-video-card-axrx-5700-8gbd6-3dheoc"

}

rx580 = {
    "XFX Radeon RX 580 8 GB GTS Black": "https://pcpartpicker.com/product/q23H99/xfx-radeon-rx-580-8gb-gts-black-video-card-rx-580p8dbdr",
    "XFX Radeon RX 580 4 GB": "https://pcpartpicker.com/product/Jy7v6h/xfx-radeon-rx-580-8gb-video-card-rx-580p427d6",
    "Gigabyte Radeon RX 580 8 GB GAMING 8G": "https://pcpartpicker.com/product/sZWBD3/gigabyte-radeon-rx-580-8-gb-gaming-8g-video-card-gv-rx580gaming-8gd-rev20"
}

with open("rx580.json", "w") as f:
    json.dump(rx580, f)