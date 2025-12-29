from find_perm import find_permission_in_dir

def find_priv_inject():
    apk_dir = r'priv-app'
    target_perm = "INJECT_EVENTS"
    
    find_permission_in_dir(target_perm, apk_dir)

def find_priv_capture():
    apk_dir = r'priv-app'
    target_perm = "CAPTURE_VIDEO"
    
    find_permission_in_dir(target_perm, apk_dir)

def find_system_app_inject():
    apk_dir = r'app'
    target_perm = "INJECT_EVENTS"
    
    find_permission_in_dir(target_perm, apk_dir)

def find_system_app_capture():
    apk_dir = r'app'
    target_perm = "CAPTURE_VIDEO"
    
    find_permission_in_dir(target_perm, apk_dir)

def main():
    find_priv_capture()
    find_system_app_inject()
    find_system_app_capture()

if __name__ == "__main__":
    main()
