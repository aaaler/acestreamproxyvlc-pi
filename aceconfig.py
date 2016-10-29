'''
AceProxy configuration script
Edit this file.
'''

import logging
import acedefconfig
from aceclient.acemessages import AceConst


class AceConfig(acedefconfig.AceDefConfig):
    # ----------------------------------------------------
    # Ace Stream Engine configuration
    # ----------------------------------------------------
    #
    # Spawn Ace Stream Engine automatically
    acespawn = True
    # Ace Stream cmd line (use `--log-file filepath` to write log)
    # Autodetect for Windows
    acecmd = "/start_acestream.sh --client-console --bind-all --live-buffer 50 --max-connections 400 --max-peers 200 --live-cache-type memory --live-cache-size 70000000"
    # Ace Stream API key
    # You probably shouldn't touch this
    acekey = 'n51LvQoTlJzNGaFxseRK-uvnvX-sD4Vm5Axwmc4UcoD-jruxmKsuJaH0eVgE'
    # Ace Stream Engine host
    # Change this if you use remote Ace Stream Engine
    # Remember that by default Ace Stream Engine listens only
    # Local host, so start it with --bind-all parameter
    acehost = 'localhost'
    # Ace Stream Engine port (autodetect for Windows)
    aceport = 62062
    # Ace Stream age parameter (LT_13, 13_17, 18_24, 25_34, 35_44, 45_54,
    # 55_64, GT_65)
    aceage = AceConst.AGE_18_24
    # Ace Stream sex parameter (MALE or FEMALE)
    acesex = AceConst.SEX_MALE
    # Ace Stream Engine startup timeout
    # On Windows Ace Engine refreshes acestream.port file only after loading GUI
    # Loading takes about ~10 seconds and we need to wait before taking port out of it
    # Set this to 0 if you don't use proxy at startup or don't need to wait
    # Only applies to Windows systems
    acestartuptimeout = 15
    # Ace Stream Engine connection timeout
    aceconntimeout = 5
    # Ace Stream Engine authentication result timeout
    aceresulttimeout = 5
    #
    # ----------------------------------------------------
    # AceProxy configuration
    # ----------------------------------------------------
    #
    # HTTP Server host
    httphost = '0.0.0.0'
    # HTTP Server port
    httpport = 8000
    # Read the video input stream in chunks of the following size    
    readchunksize = 8192
    # Cache the following number of the tailing chunks
    readcachesize = 1000
    # If started as root, drop privileges to this user.
    # Leave empty to disable.
    aceproxyuser = 'aceproxy'
    # Enable firewall
    firewall = False
    # Firewall mode. True for blackilst, False for whitelist
    firewallblacklistmode = False
    # Network ranges. Please don't forget about comma in the end
    # of every range, especially if there is only one.
    firewallnetranges = (
        '127.0.0.1',
        '10.0.0.0/8',
        )
    # Maximum concurrent connections (video clients)
    maxconns = 10
    #
    # ----------------------------------------------------
    # VLC configuration
    # ----------------------------------------------------
    #
    # Use VideoLAN VLC Media Player
    # I strongly recommend to use VLC, because it lags a lot without it
    # And multiple clients can't watch one stream without it.
    # That's Ace Stream Engine fault.
    # To use this, you should install VLC first
    # And run it with:
    # vlc -I telnet --clock-jitter 0 --network-caching 500 --telnet-pass admin
    vlcuse = True
    # Use AceStream player that comes with engine
    # If true than proxy will detect a path to ace_player.exe and ace_player.exe will be spawned
    # It also will not check if vlc.exe is running, it will watch over ace_player.exe process
    # This option applies only for Windows systems
    # If set to true, you need to edit vlccmd like this:
    # ace_player.exe -I telnet --clock-jitter -1 --network-caching -1 --sout-mux-caching 2000 --telnet-password admin
    # to point ace_player.exe, not vlc.exe!!!
    vlcuseaceplayer = False
    # Spawn VLC automaticaly
    vlcspawn = True
    # VLC cmd line (use `--file-logging --logfile=filepath` to write log)
    # Please use the full path to executable for Windows, for example - C:\\Program Files\\VideoLAN\\VLC\\vlc.exe
    vlccmd = "vlc -I telnet --clock-jitter -1 --network-caching -1 --sout-mux-caching 2000 --telnet-password admin --telnet-port 4212"
    # VLC spawn timeout
    # Adjust this if you get error 'Cannot spawn VLC!'
    vlcspawntimeout = 30
    # VLC host
    vlchost = '127.0.0.1'
    # VLC telnet interface port
    vlcport = 4212
    # VLC streaming port (you shouldn't set it in VLC itself)
    vlcoutport = 8011
    # VLC telnet interface password
    vlcpass = 'admin'
    # Pre-access (HTTP) VLC parameters
    # You can add transcode options here
    # Something like #transcode{acodec=mpga,ab=128,channels=2,samplerate=44100}
    vlcpreaccess = ''
    # VLC muxer. You probably want one of these streamable muxers:
    # ts, asf, flv, ogg, mkv
    # You can use ffmpeg muxers too, if your VLC is built with it
    # ffmpeg{mux=NAME} (i.e. ffmpeg{mux=mpegts})
    # VLC's ts muxer sometimes can work badly, but that's the best choice for
    # now.
    vlcmux = 'ts'
    # Force ffmpeg INPUT demuxer in VLC. Sometimes can help.
    vlcforceffmpeg = False
    # Stream start delay for dumb players (in seconds)
    # !!!
    # PLEASE set this to 0 if you use VLC
    # !!!
    #
    # ----------------------------------------------------
    # Transcoding configuration
    # ----------------------------------------------------
    # Enable/disable transcoding
    transcode = False
    # Dictionary with a set of transcoding commands. Transcoding command is an 
    # executable commandline expression that reads an input stream from STDIN 
    # and writes a transcoded stream to STDOUT. The commands are selected 
    # according to the value of the 'fmt' request parameter. For example, the 
    # following url:
    # http://loclahost:8000/channels/?type=m3u&fmt=mp2
    # contains the fmt=mp2. It means that the 'mp2' command will  be used for 
    # transcoding. You may add any number of commands to this dictionary.
    transcodecmd = dict()
    # transcodecmd['100k'] = 'ffmpeg -i - -c:a copy -b 100k -f mpegts -'
    # transcodecmd['mp2'] = 'ffmpeg -i - -c:a mp2 -c:v mpeg2video -f mpegts -qscale:v 2 -'.split()
    # transcodecmd['mkv'] = 'ffmpeg -i - -c:a copy -c:v copy -f matroska -'.split()
    # transcodecmd['default'] = 'ffmpeg -i - -c:a copy -c:v copy -f mpegts -'.split()
    
    # ----------------------------------------------------
    videodelay = 0
    # Obey PAUSE and RESUME commands from Engine
    # (stops sending data to client, should prevent annoying buffering)
    # !!!
    # PLEASE set this to False if you use VLC
    # !!!
    videoobey = False
    # Stream send delay after PAUSE/RESUME commands (works only if option
    # above is enabled)
    # !!!
    # PLEASE set this to 0 if you use VLC
    # !!!
    videopausedelay = 0
    # Seek back feature.
    # Seeks stream back for specified amount of seconds.
    # Greatly helps fighing AceSteam lags, but introduces
    # video stream delay.
    # Set it to 30 or so.
    # Works only with the newest versions of AceEngine!
    videoseekback = 0
    # Delay before closing Ace Stream connection when client disconnects
    # In seconds.
    videodestroydelay = 30
    # Pre-buffering timeout. In seconds.
    videotimeout = 40
    #
    # Some video players (mostly STBs and Smart TVs) can generate dummy requests
    # to detect MIME-type or something before playing which Ace Stream handles badly.
    # We send them 200 OK and do nothing.
    # We add their User-Agents here
    fakeuas = ('Mozilla/5.0 IMC plugin Macintosh', )
    #
    # Some video players have very short timeout and can disconnect from the proxy
    # before the headers sent.
    # We send them 200 OK and MPEG MIME-type right after connection has been initiated
    fakeheaderuas = ('HLS Client/2.0 (compatible; LG NetCast.TV-2012)',
                     'Mozilla/5.0 (DirectFB; Linux armv7l) AppleWebKit/534.26+ (KHTML, like Gecko) Version/5.0 Safari/534.26+ LG Browser/5.00.00(+mouse+3D+SCREEN+TUNER; LGE; 42LM670T-ZA; 04.41.03; 0x00000001;); LG NetCast.TV-2012 0'
                     )

    # Logging configuration
    #
    # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    loglevel = logging.DEBUG
    # Log message format
    logfmt = '%(asctime)s %(levelname)s %(threadName)s %(filename)s:%(lineno)d %(name)s| %(message)s'
    # Log date format
    logdatefmt='%d.%m %H:%M:%S'
    # Full path to a log file
    logfile = None 
    
    # This method is used to detect fake requests. Some players send such 
    # requests in order to detect the MIME type and/or check the stream availability.
    @staticmethod
    def isFakeRequest(path, params, headers):
        useragent = headers.get('User-Agent')
        
        if not useragent:
            return False
        elif useragent in AceConfig.fakeuas:
            return True
        elif useragent == 'Lavf/55.33.100' and not headers.has_key('Range'):
            return True
        elif useragent == 'GStreamer souphttpsrc (compatible; LG NetCast.TV-2013) libsoup/2.34.2' and headers.get('icy-metadata') != '1':
            return True
