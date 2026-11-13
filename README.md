# GhostMic360 👻🎙️

Experimental voice-announcement project for Xbox 360 RGH.

**Status:** Offline Python prototype. There is **no working Xbox 360 .xex, virtual microphone, Kinect emulation, or voice-chat transmission** yet.

## Goal
Manually trigger a short multilingual warning in a game's existing voice chat, without a physical Kinect or headset if technically possible. Initial research target: Plants vs. Zombies: Garden Warfare (Xbox 360). Player identification is intentionally out of scope.

## Try the offline prototype
```sh
python src/ghostmic.py --lang pt
python src/ghostmic.py --lang es --wav audio/alert.wav
```
The script prints a warning and optionally checks a prerecorded PCM WAV file. It does not synthesize speech or send audio to the Xbox.

## Research
- [xsdk](https://github.com/xenosworks/xsdk): community Xbox 360 SDK.
- [RXDK360-Samples](https://github.com/Team-Resurgent/RXDK360-Samples): audio API examples to investigate.
- [xbdm](https://github.com/copeison/xbdm): debugging.
- [XEXLoaderWV](https://github.com/zeroKilo/XEXLoaderWV): XEX analysis.
- XHV2: Xbox 360 voice chat research direction, not verified for GW1.
- XAudio2: playback is not the same as microphone/chat transmission.

## Roadmap
1. Prepare a short PCM WAV with Android text-to-speech.
2. Verify local audio playback on an RGH Xbox 360.
3. In a private test, check whether the game initializes voice capture without a physical input device.
4. Only if feasible, investigate virtual capture injection and test with consenting players.
5. Respect the game's normal voice scope; there is no confirmed method to reach both teams.

Use short, manual, rate-limited announcements and neutral wording about **suspected** cheating. No network attacks, player targeting, or spam.

Licensed under the MIT software license.
