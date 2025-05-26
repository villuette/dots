config.bind('<Alt-u>', 'spawn --userscript  qute-keepassxc --key B00AA8A3BB7B69B2', mode='insert')
config.bind('pw', 'spawn --userscript ~/.config/qutebrowser/.venv/bin/python .config/qutebrowser/qute-keepassxc --key B00AA8A3BB7B69B2', mode='normal')
config.bind('<Ctrl-c>', 'mode-enter normal', mode='insert')
# Алиасы для переключения
c.aliases["proxyon"] = "set content.proxy socks://127.0.0.1:1080"
c.aliases["proxyoff"] = "set content.proxy none"

config.load_autoconfig()
