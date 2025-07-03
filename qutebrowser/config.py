c.tabs.show = "multiple"


c.tabs.title.format = "{audio}{current_title}"
c.fonts.web.size.default = 20

config.load_autoconfig(False)  # load settings done via the gui

c.auto_save.session = True  # save tabs on quit/restart

# dark mode setup
c.colors.webpage.darkmode.enabled = False
c.colors.webpage.darkmode.algorithm = "lightness-cielab"
c.colors.webpage.darkmode.policy.images = "never"
config.set("colors.webpage.darkmode.enabled", False, "file://*")

# styles, cosmetics
c.tabs.padding = {"top": 5, "bottom": 5, "left": 9, "right": 9}
c.tabs.indicator.width = 0  # no tab indicators
c.tabs.width = "7%"

# fonts
c.fonts.default_family = []
c.fonts.default_size = "13pt"
c.fonts.web.family.fixed = "FontMono Nerd Font"
c.fonts.web.family.sans_serif = "FontMono Nerd Font"
c.fonts.web.family.serif = "FontMono Nerd Font"
c.fonts.web.family.standard = "FontMono Nerd Font"

# privacy - adjust these settings based on your preference
# config.set("completion.cmd_history_max_items", 0)
# config.set("content.private_browsing", True)
config.set("content.webgl", False, "*")
config.set("content.geolocation", False)
config.set("content.webrtc_ip_handling_policy", "default-public-interface-only")
config.set("content.cookies.accept", "all")
config.set("content.cookies.store", True)
# config.set("content.javascript.enabled", False) # tsh keybind to toggle
#
c.content.blocking.enabled = True

# keybinds
config.bind("sH", "config-cycle statusbar.show always never")

# Set the main window to allow transparency (optional, but may help with overall window transparency)
c.window.transparent = True

# Set the tab bar background to transparent
c.colors.tabs.bar.bg = "rgba(0, 0, 0, 0.4)"  # 50% transparent black

# Set background for unselected even and odd tabs
c.colors.tabs.even.bg = "rgba(0, 0, 0, 0.55)"  # 50% transparent black
c.colors.tabs.odd.bg = "rgba(0, 0, 0, 0.55)"  # 50% transparent black

# Set background for selected even and odd tabs
c.colors.tabs.selected.even.bg = "rgba(0, 0, 0, 0.85)"  # Slightly less transparent
c.colors.tabs.selected.odd.bg = "rgba(0, 0, 0, 0.85)"  # Slightly less transparent

# Optional: Set foreground (text) colors for better visibility
c.colors.tabs.even.fg = "rgba(255, 255, 255, 0.8)"  # Semi-transparent white
c.colors.tabs.odd.fg = "rgba(255, 255, 255, 0.8)"  # Semi-transparent white
c.colors.tabs.selected.even.fg = "white"  # Solid white for selected tabs
c.colors.tabs.selected.odd.fg = "white"  # Solid white for selected tabs

# Set the status bar background to semi-transparent
c.colors.statusbar.normal.bg = "rgba(0, 0, 0, 0.6)"  # 50% transparent black
c.colors.statusbar.insert.bg = (
    "rgba(0, 0, 0, 0.6)"  # 50% transparent black in insert mode
)
c.colors.statusbar.command.bg = (
    "rgba(0, 0, 0, 0.6)"  # 50% transparent black in command mode
)
c.colors.statusbar.passthrough.bg = (
    "rgba(0, 0, 0, 0.6)"  # 50% transparent black in passthrough mode
)

# Optional: Set foreground (text) colors for better visibility
c.colors.statusbar.normal.fg = "rgba(255, 255, 255, 0.8)"  # Semi-transparent white
c.colors.statusbar.insert.fg = "rgba(255, 255, 255, 0.8)"  # Semi-transparent white
c.colors.statusbar.command.fg = "rgba(255, 255, 255, 0.8)"  # Semi-transparent white
c.colors.statusbar.passthrough.fg = "rgba(255, 255, 255, 0.8)"  # Semi-transparent white
