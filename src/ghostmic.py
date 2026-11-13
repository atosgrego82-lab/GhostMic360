#!/usr/bin/env python3
"""GhostMic360 offline audio-announcement prototype; NOT an Xbox mic emulator."""
import argparse
from pathlib import Path
import wave

MESSAGES = {
    "pt": "Atenção, jogadores. Há suspeita de trapaça nesta partida. Verifiquem o placar e denunciem comportamentos suspeitos.",
    "es": "Atención, jugadores. Hay sospechas de trampas en esta partida. Revisen el marcador y reporten conductas sospechosas.",
    "en": "Attention, players. Cheating is suspected in this match. Check the scoreboard and report suspicious behavior.",
}

def inspect_wav(path: Path) -> str:
    with wave.open(str(path), "rb") as audio:
        if audio.getcomptype() != "NONE":
            raise ValueError("Expected uncompressed PCM WAV")
        return (
            f"PCM WAV: {audio.getnchannels()} channel(s), "
            f"{audio.getframerate()} Hz, "
            f"{audio.getsampwidth() * 8}-bit, "
            f"{audio.getnframes()} frames"
        )

def main() -> None:
    parser = argparse.ArgumentParser(description="GhostMic360 offline prototype")
    parser.add_argument("--lang", choices=MESSAGES, default="pt")
    parser.add_argument("--wav", type=Path, help="Inspect a prerecorded PCM WAV")
    args = parser.parse_args()
    print(MESSAGES[args.lang])
    if args.wav is not None:
        print(inspect_wav(args.wav))
    print("Offline only: no Xbox microphone emulation or voice-chat transmission.")

if __name__ == "__main__":
    main()
