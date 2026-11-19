[app]

# (str) Title of your application
title = CLAUDE CODE

# (str) Package name
package.name = claudecode

# (str) Package domain (needed for android packaging)
package.domain = org.god

# (str) Source files to include (let it separate with commas)
source.include_exts = py,png,jpg,kv,atlas

# (str) Source directory where the application files are located
source.dir = .

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,requests

# (str) Supported orientations
orientation = portrait

# (int) Fullscreen (1 = fullscreen, 0 = not fullscreen)
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (bool) Automatically accept Android SDK license
android.accept_sdk_license = True

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android NDK version
android.ndk = 23b

# (int) Log level
log_level = 2
