# These and other macros are documented in dhd/droid-hal-device.inc
%define device sagit
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Mi 6 (sagit)
%define installable_zip 1
%define droid_target_aarch64 1

%define straggler_files \
/init.qcom.sensors.sh\
/init.qcom.sh\
/init.qcom.early_boot.sh\
/init.qcom.usb.sh\
/bugreports\
/cache\
/d\
/file_contexts.bin\
/property_contexts\
/sdcard\
/selinux_version\
/service_contexts\
/vendor\
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc
