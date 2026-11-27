# Bomb 3D Simulator — Game Spec

Designed by the kid (two pencil sketches + Q&A), built with Claude.

## The world (sketch 1)
- A round **hub** in the middle where "me & my friends" start.
- **8 islands** around the hub, each joined to it by a **striped bridge**.
- Water all around, tall stone pillars in the background.
- The ground is made of blocky tiles, so bombs can **blow holes** in islands and bridges.
  Fall into the water = splash, lose 20 health, respawn on the hub.
- Islands rebuild between waves.

## Tutorial (for new players)
- A brand-new player who presses **Start** plays the tutorial first. Anyone can replay it with the **Tutorial** button in the menu.
- It's a practice round on the hub with **Coach**: you can't get hurt, the ground doesn't break, and each step moves on once you've done it:
  1. Walk around  2. Look around  3. Jump two times  4. Grab a falling bomb  5. Run into Coach to pass it
  6. Grab a bomb and throw it far away  7. Watch Coach get a black face and be out (press "Got it!")
  8. Grab a coin and a shield  9. "You're ready!" → Let's play!
- The controls shown match the device: keys on a computer, joystick and buttons on a phone. Every step can be skipped.

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

## Healing ground
- Every map has **3 healing pads**, far away near the edges of the map: glowing aqua ground with a light beam and a spinning green **+** above it.
- Stand on one to heal about **10 health per second** (green sparkles; your health bar glows). Buddies and multiplayer friends heal too.
- Bombs can break the pads like any ground; they rebuild between waves. "Healing ground!" shows the first time you step on one in a level.

## Levels (5,000)
- Levels 1–5,000, in pages of 20 in the menu (« ‹ › » buttons). **All levels are unlocked**: pick any one.
- It gets harder up to level 50 (more bombs, faster, more of the special bombs), then stays that hard.
- Every 5th level is a boss level. The boss needs at most 14 hits.

## How to play
- **Goal:** survive **all the waves** of a level. Level 1 has 3 waves; later levels have more (up to 8).
- **Health bar:** 100 health. Bombs hurt. 0 health = game over (try again).
- **Bombs fall from the sky in waves.** A red circle shows where each one will land.
- **Hot potato!** Go near a bomb that has landed and you **grab it automatically**. A countdown
  (starting at 7 seconds) shows above it. **Touch someone else to pass it** (you get +1 coin);
  passing doesn't reset the timer, but whoever gets it always has at least 2 seconds. If the timer runs out while you hold it,
  **it explodes in your face**. You can also press E to throw it away.
- **Black face = you're out!** Whoever is holding the bomb when it explodes is knocked out at once.
  In single player that's game over; buddies (and players in multiplayer) come back next wave.
- When a bomb explodes in someone's hands, **their whole head turns sooty black** (white eyes and smile)
  and smokes, and stays black while they're out. If it's you, the camera swings round for a moment to show your face.
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
- **Flying capes** (in the Shop): jump, then **hold Jump** — every cape flies for as long as you hold it (up to the sky limit).
  - Glider Cape — 300: fly, glide down slowly
  - Hero Cape — 1,000: climbs faster, double jump, faster in the air
  - Super Cape — 2,500: climbs faster still, double jump
  - Rainbow Cape — 6,000: fastest climbing and flying
  The cape flaps on your back.
- **RPGs** (in the Shop, expensive!): shoot bombs away. Press **F** or right-click (phone: **Fire** button).
  A rocket flies at the nearest bomb in front of you and pops it harmlessly in confetti (+1 coin); rockets hit the boss too.
  - Rusty RPG — 500 coins: reload 3 s, aims when fired
  - Turbo RPG — 1,200: reload 1.8 s, homing
  - Mega RPG — 2,500: reload 1 s, strong homing, pops every bomb near the one it hits
  - Golden RPG — 5,000: reload 0.5 s, fires 3 rockets at once, strongest homing
  You always use your best RPG; it shows on your shoulder and its reload bar is in the HUD.
- **Health upgrades** (top of the Shop): 8 upgrades of +25 max health each, from 100 up to 300.
  Prices: 30, 60, 100, 150, 220, 300, 400, 500 coins. Hearts show how many you've bought; the health bar shows e.g. 175 / 175.

## Multiplayer
- Menu → **Mode → Multiplayer** → **Create game** gives a 4-letter code. Friends tap Multiplayer, type the code and press **Join**.
  "Check who's in the server" lists everyone who has the game open right now, with a **Join** button.
- The host picks the level and map, then presses **Start**: everyone plays the same level together, hot potato included.
  Pass the bomb to your real friends!
- Players who are out come back next wave. The level is lost only when every player is out.
- Friends need the game's link shared with them (Share menu) and must open it on claude.ai while signed in.
- How it works: the host's game runs everything and shares it live through the claude.ai room;
  each friend's game only moves its own character. If the host leaves, the game ends.

## Username Maker
- A **Username** card in the menu: type your own name (as long as you like) or press **Make me one!**,
  which spins through funny names (like *TurboPickle42*) made only from kid-friendly bomb-themed words.
- Your username floats above your character and is what friends see in multiplayer.

## Pet shop (50 pets, evolutions and ranks)
Menu → **Pet shop**. Buy pets (120 to 10,000 coins), then pick one to bring along (or "No pet"). Your pet follows you and helps.
- **Ranks** (by how special a pet is): Common < 500 · Uncommon < 1,000 · Rare < 2,000 · Epic < 4,000 · Legendary < 7,000 · Mythic 7,000+.
  Shown as a coloured badge and card border, and on the in-game pet chip.
- **Powers** (9 kinds): pulls coins to you · heals you · warns about bombs landing near you (red "!") · blocks hits now and then ·
  breathes fire to pop bombs · extra XP · run faster · sometimes doubles coins · double jump. Pricier pets have stronger powers.
- **Evolutions**: every pet has 3 stages — *Pet* → *Super Pet* → *Mega Pet*. The pet you bring earns pet XP (the same XP you earn);
  150 XP lets it evolve to Super, 500 to Mega. Press **Evolve!** in the Pet shop. Evolved pets are bigger, get a gold collar
  (Super) or a crown, glow and sparkles (Mega), and their power gets 40% / 80% stronger.
- Pets are built from body types: four-legged animals, birds, turtles, dragons, horses (unicorn, pegasus), slimes, robots, fish and ghosts.
- In multiplayer, guests' pets mostly just look cute (warnings and XP boosts still work).

## XP
- Earn XP: pass a bomb +5 · pop a bomb with an RPG +3 · thrown bomb explodes far away +2 · coin +1 · power-up +5 ·
  survive a wave +20 · hit the boss +15 · beat the boss +100 · beat a level +50 (+1 per level number, up to +100) ·
  lose a level +10 · finish the tutorial +50.
- Fill the XP bar to **LEVEL UP** (XP level 1 → 2 needs 100 XP, then 50 more each level) and get 10 × your new XP level in coins.
- XP bar with your XP level badge under the health bar, and in the Username card in the menu.

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
- **Levels** 1–5,000 in pages (all unlocked) and a **Maps** picker.
- **Volume** slider and **Vibration** on/off.
- **Languages:** English, Español, Français, Deutsch, Português, हिन्दी, 中文, 日本語.
- **Mode:** Single player or Multiplayer (create a game or join with a code).
- **Check who's in the server**, **Add friends** and **Make a friend** (name your buddies, up to 7).
- **Settings**, **Shop**.
- Progress, coins, items and settings are saved in the browser.


## Tech
- One file: `bomb3d/index.html`, using Three.js (r128 from cdnjs). No build step.
- Sounds are made in code (Web Audio), so there are no asset files.
