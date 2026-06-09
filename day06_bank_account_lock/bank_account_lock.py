username = "SilentAstronaut"
password = "Stars4Life"
locked = True

new_pwd = "GalaxyGo!"
confirm_pwd = "GalaxyGo!"

if new_pwd == confirm_pwd:
    password = new_pwd
    print("✅ Password changed")

    pwd_changed = True
else:
    print("Passwords don't match")

    pwd_changed = False


if pwd_changed:
    print("🔓 Account unlocked")
    locked = False
else:
    print("Try again")