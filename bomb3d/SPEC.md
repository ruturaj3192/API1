# Bomb 3D Simulator — Game Spec

Designed by the kid (two pencil sketches + Q&A), built with Claude.

## The world (sketch 1)
- A round **hub** in the middle where "me & my friends" start.
- **8 islands** around the hub, each joined to it by a **striped bridge**.
- Water all around, tall stone pillars in the background.
- The ground is made of blocky tiles, so bombs can **blow holes** in islands and bridges.
  Fall into the water = splash, lose 20 health, respawn on the hub.
- Islands rebuild between waves.

## Maps (11)
Pick one in the menu's **Maps** box. Every level is played on the map you pick.
- **Bomb Islands**: the original hub with 8 islands and striped bridges.
- **Frosty Peaks**: 6 snowy islands. **Slippery ice!**
- **Lava Lake**: a ring bridge round 4 rock islands over lava. Falling in hurts more (35).
- **Candy Donut**: a sprinkle-donut ring, candy-cane bridges, lollipops, a chocolate lake.
- **Desert Oasis**: a giant sand cross with oasis pools and cactuses.
- **Space Station**: 9 metal platforms with laser walkways. **Low gravity**; fall off and you drop into space.
- **Jungle Spiral**: a long spiral path with vine bridges cutting across.
- **Rainbow Ring**: a rainbow ring around the hub with rainbow bridges.
- **Raft Party**: lots of little rafts. **Jump from raft to raft.**
- **Spooky Graveyard**: night time, tombstones, open graves (holes) and green slime.
- **Cloud Kingdom**: cloud islands with golden bridges and little towers. **Floaty jumps.**

## Levels (5,000)
- Levels 1–5,000, in pages of 20 in the menu (« ‹ › » buttons). Beat a level to unlock the next one.
- It gets harder up to level 50 (more bombs, faster, more of the special bombs), then stays that hard.
- Every 5th level is a boss level. The boss needs at most 14 hits.

## How to play
- **Goal:** survive **all the waves** of a level. Level 1 has 3 waves; later levels have more (up to 8).
- **Health bar:** 100 health. Bombs hurt. 0 health = game over (try again).
- **Bombs fall from the sky in waves.** A red circle shows where each one will land.
- **Hot potato!** Go near a bomb that has landed and you **grab it automatically**. A countdown
  (starting at 7 seconds) shows above it. **Touch someone else to pass it** (you get +1 coin);
  passing doesn't reset the timer, but whoever gets it always has at least 2 seconds. If the timer runs out while you hold it,
  **it explodes in your face** (extra damage). You can also press E to throw it away.
- When a bomb explodes in someone's hands, **their whole head turns sooty black** (white eyes and smile)
  and smokes for about 6 seconds. If it's you, the camera swings round for a moment to show your face.
- Buddies play hot potato too: a buddy with a bomb **chases the nearest person** (you too!)
  to pass it, and the others run away from them.
- **Bomb types** (unlock as levels go up):
  - Normal (black) — level 1+
  - Mega (red, huge blast) — level 3+
  - Cluster (purple, splits into 4 in the air) — level 5+
  - Sticky (green, drifts toward people while falling) — level 7+
- **Boss bomb:** every 5th level ends with a giant boss bomb flying over the islands and
  dropping bombs. Grab bombs and throw them at it (throws auto-aim at the boss) to win.
- **Power-ups** on the islands: Shield (no damage), Speed boots, Double jump, Heal.
- **Coins:** spin on the islands, plus bonuses for each wave and level and for throwing bombs.
- **Shop:** spend coins on hats and shirt/hair colours.

## Characters
- You and your friends are blocky characters with **bacon hair**.
- **Third-person camera** behind you.
- Computer-controlled **buddies** run around and dodge bombs too. If they get knocked out,
  they come back next wave. Name tags float over them.

## Controls (Mac and phone/iPad)
- Mac: **WASD / arrow keys** move, **Space** jumps, **Shift** runs,
  **drag the mouse** to turn the camera, **E** grabs and throws, **Esc/P** pauses.
- Touch: joystick (left), drag right side to look, **Jump** and **Grab/Throw** buttons.

## Menu (sketch 2)
- Title **Bomb 3D Simulator**, big **Start** button, **Exit** button.
- **Levels** 1–5,000 in pages (unlock one by one) and a **Maps** picker.
- **Volume** slider and **Vibration** on/off.
- **Languages:** English, Español, Français, Deutsch, Português, हिन्दी, 中文, 日本語.
- **Mode:** Single player (now); Multiplayer is shown as "coming soon".
- **Check who's in the server**, **Add friends** and **Make a friend** (name your buddies, up to 7).
- **Settings**, **Shop**.
- Progress, coins, items and settings are saved in the browser.

## Not yet (later ideas)
- Real online multiplayer with friends on their own computers (needs a game server).

## Tech
- One file: `bomb3d/index.html`, using Three.js (r128 from cdnjs). No build step.
- Sounds are made in code (Web Audio), so there are no asset files.
