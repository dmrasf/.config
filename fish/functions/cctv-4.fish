# Defined in - @ line 1
function cctv-4 --description 'CCTV-4'
    mpv http://117.169.120.140:8080/live/cctv-4/.m3u8 > /dev/null 2>&1 &
end
