# Bomb 3D Simulator — Game Spec

Designed by the kid (two pencil sketches + Q&A), built with Claude.

## Backstory — "The Story of Boomtopia"
A 6-page picture book (menu → **Story**; brand-new players see it once before the tutorial):
1. Long ago, Boomtopia was a happy land of floating islands where kids with bacon hair played every day.
2. Then the **Bomb King** woke up inside the volcano — grumpy, fuse always lit, and he hated fun.
3. He made bombs rain from the sky, wave after wave, to blow up the islands.
4. The kids found a trick: bombs only explode when the timer runs out — pass them like a hot potato!
   Hold one too long and your face goes black, and you're out.
5. The islands fought back: healing grounds began to glow, brave pets joined the team, and the shop sold capes and RPGs.
6. Now it's your turn: survive all 5,000 levels, beat the Bomb King every 5th level, and bring the fun back to Boomtopia!
The boss is the Bomb King ("BOMB KING!" appears when he arrives).

## The mission: bring everyone back to Boomtopia
- The Bomb King trapped Boomtopia's **10,000 people** (kids **and grownups**) in bubbles and scattered them across the islands.
- Every level hides **6 trapped bubbles** on the far islands (glowing bubbles with a "Help!" sign), and **2 more** appear after every wave.
  About 1 in 3 is a big **family bubble** (2 grownups + 1–2 kids) that frees 3–4 people at once. Touch a bubble to pop it:
  everyone inside flies home to the city, and you get coins and XP. Each **boss holds 10 more**, freed when you beat it.
- The menu's **Mission** card shows how many of the 10,000 you've brought back; the HUD shows "People: 4 / 11" for the level.
- Rescuing all 10,000: "You saved Boomtopia!", fireworks and a big coin reward. Achievements: Rescuer (10), Hero (100),
  Super Hero (1,000), Savior of Boomtopia (10,000).
- The story's pages 3 and 6 now tell this mission.

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

## Maps (20)
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
- **Volcano Island**: rings of rock split by **lava rivers**, with bridges across the lava moat.
- **Mushroom Forest**: giant mushroom caps at dusk — jump from mushroom to mushroom.
- **Pirate Cove**: a big pirate-ship deck with gangplanks to palm-tree islands.
- **Crystal Caves**: a glowing purple star floating in the dark — don't fall off!
- **Toy Town**: colourful toy-brick blocks with little gaps and two roads.
- **Beach Party**: a sandy beach with a lagoon, a pier and palm trees.
- **Moon Base**: grey moon ground with craters and **super low gravity**.
- **Cheese Land**: a giant holey cheese in a lake of milk.
- **Ninja Dojo**: wooden walkways and little platforms with red lanterns.

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
- **Boss bomb (the Bomb King):** every 5th level ends with a giant boss bomb flying over the islands and
  dropping bombs. Grab bombs and throw them at it (throws auto-aim at the boss) to win.
- **Power-ups** on the islands (11, each with its name floating above it):
  Shield (no damage) · Speed boots · Double jump · Heal ·
  **Magnet** (pulls coins to you, 12 s) · **Giant** (you grow big: no knockback, half damage, 10 s) ·
  **Freeze** (every bomb freezes in place and timers pause, 6 s) · **Super jump** (12 s) ·
  **Cloud walk** (walk on air over holes, water and lava, 10 s) · **Double coins** (20 s) ·
  **Force field** (a pink ring that pushes falling bombs away from you, 10 s).
- **Coins:** spin on the islands (14 per level, 9 more each wave), plus bonuses for passing, popping and throwing bombs,
  each wave, each level, bosses and XP level-ups. **Every coin reward is worth 4×**, so saving up for the shop is quick.
- **Shop:** spend coins on hats and shirt/hair colours.
- **Flying capes** (in the Shop): jump, then **hold Jump** — every cape flies for as long as you hold it, with **no height limit**.
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
- **Health upgrades** (top of the Shop): 25 upgrades, from 100 up to **2,000** max health.
  The first 8 give +25 each (30–500 coins), the next 17 give +100 each (650–6,250 coins).
  Healing pads, Heal power-ups and wave breaks heal a share of your max health, so they still help at 2,000.

## Multiplayer
- Menu → **Mode → Multiplayer** → **Create game** gives a 4-letter code. Friends tap Multiplayer, type the code and press **Join**.
  "Check who's in the server" lists everyone who has the game open right now, with a **Join** button.
- The host picks the level and map, then presses **Start**: everyone plays the same level together, hot potato included.
  Pass the bomb to your real friends!
- **Chat** (multiplayer): quick-chat buttons ("Hi!", "Pass it to me!", "Run!", "Help!", "Nice!", "Good game!", "Follow me!", "Haha!")
  or type your own message (80 letters max). Open it with the chat button, **Enter** or **T** in a game, or use the chat box in the
  Multiplayer menu while waiting. Messages show in a chat list and as a speech bubble over the player's head.
  A simple filter hides rude words and website links (it can't catch everything — only share the game with friends you know).
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

## Daily rewards
- A 7-day calendar pops up once a day (or menu → More fun → Daily reward): 100, 150, 200, 300, 400, 600 coins,
  then a **mystery gift** on day 7 (a free pet, 1,500 coins or 500 XP). Missing a day starts again at day 1.

## Achievements (17)
- Menu → More fun → Achievements. Each has a progress bar and pays coins (100–3,000) when unlocked, with a gold
  "Achievement unlocked!" pop-up. Examples: Hot Hands (pass 10 bombs), Potato Legend (pass 1,000), Rocket Rain (pop 250),
  Boss Slayer, Royal Pain (beat 10 bosses), Wave Rider, Unstoppable (beat 100 levels), Treasure Hunter, Zookeeper (25 pets),
  Sooty Face (10 black faces), Rising Star (XP level 10).

## Bosses (8, taking turns every 5th level)
- **Bomb King** (levels 5, 45, 85…): the original.
- **Ice King** (10, 50…): icy blue; his bombs **freeze** you (half speed for 3 s).
- **Rocket Queen** (15, 55…): magenta with rocket boosters; throws bombs much faster, often two at once.
- **Lava Lord** (20, 60…): glowing red-hot with a flame crown; throws lots of huge mega bombs.
- **Ghost Bomb** (25, 65…): see-through; fades away and **teleports**, throws sticky bombs that chase you.
- **Robo Bomber** (30, 70…): shiny metal with red robot eyes; drops cluster bombs that split into 4.
- **Thunder Bomb** (35, 75…): purple with a lightning crown; **lightning strikes** — super-fast bombs with a flash of lightning.
- **Bomb Emperor** (40, 80…): huge, with a gold crown, jewels and belt; uses everyone's attacks and has extra health (up to 21 hits).
Each boss has its own fight music. Throw bombs (or shoot RPGs) at them to win.

## Emotes
- In a game: press **1–4** or the smiley button: **Wave, Dance, Spin, Cheer**. Friends see your emotes in multiplayer;
  buddies cheer when a wave ends.

## Leaderboard
- Menu → More fun → Leaderboard: everyone who has the game open right now, ranked by XP level (then levels beaten).

## Music
- Chiptune music made in code: a menu song, a different song for each of the 20 maps, and a faster boss-fight song.
  Turn it on/off in Settings → Music (it also follows the Volume slider).

## Map details and the city
- Every map sits just off the coast of **the city of Boomtopia**: a ring of **90 skyscrapers** with windows, rooftop antennas and
  blinking lights (lit windows on night maps; far below on floating maps).
- The city stands **on land, never in the water**: a stone quay around the sea, a ring road with yellow lines,
  sidewalks and street lamps. You can walk on the city land (the skyscrapers and pillars are on it, not in the sea).
- **Cars on the road:** cars, taxis, buses, a police car with flashing lights and an ice-cream truck drive around the ring
  road in two lanes going opposite ways, with spinning wheels and headlights. Stand in the road and a car honks and bumps
  you out of the way (no damage).
- **Stand on the cars:** jump onto any car, taxi, bus, police car or ice-cream truck and ride it around the city.
  First ride each level: "Car surfing!" and a few coins. Riders on top don't get bumped.
- **Trains:** an elevated railway on tall columns runs above the middle of the ring road. Two steam trains (a red engine with
  4 coaches, a blue engine with 3) go round and round, puffing smoke, whistling "choo-choo" and chuffing when you're nearby.
  Stand on the track or jump on top of a train to ride it ("Train surfing!" + coins on the first ride each level).
  Standing on the track in front of a train gets you bumped off (no damage).
- **Helicopters:** a red rescue helicopter and a blue news helicopter fly round above the edge of the city (opposite
  ways, gently bobbing), with spinning main and tail rotors, a "thup-thup" sound when near, and searchlights on night maps.
  Fly up with a cape and land on top to ride ("Helicopter ride!" + coins on the first ride each level). Riders move up and
  down with the helicopter, and the blades spin above their heads.
- **The Mayor of Boomtopia (Mayor Boomsworth):** stands on a little stage with a microphone by the sea, in front of
  **City Hall** (white columns, a golden dome and a waving flag; you can climb it and stand on its roof). He wears a top hat,
  a red sash, a gold medal and a mustache. Walk up to him and he talks in a speech bubble ("Welcome, hero!" and your task).
  Every time you rescue someone he jumps, claps and says "Thank you, hero!".
- **Mayor's task (one per level, shown in the HUD):** Rescue 4 people · Ride on a car · Ride on a train · Climb to a rooftop
  (taking turns by level). Finishing it: "The Mayor says: Thank you, hero!", coins, XP, fireworks and the crowd cheers.
- **The cheering crowd:** people of Boomtopia stand on the sidewalk by the road. Every time you rescue someone (1, 2, 3, 4
  people or a boss's 10), they jump, clap and cheer, with clapping sounds and confetti. More people saved = longer cheering.
- Textured ground blocks, flowing water/lava/slime with foam, and themed little details on every map
  (grass and flowers, snow piles, glowing embers, gumdrops and sprinkles, toy-brick studs, shells and starfish, mushrooms, crystals, rocks…).
- Floating particles: snowflakes, rising embers, fireflies, pollen or blowing dust, depending on the map.

## Your place, missions, new places and modes
**Your house** (on the city land, with a fenced yard): the Shop's **My House** section sells furniture: Cozy Bed, Big TV,
Comfy Sofa, Trophy Shelf (shows your trophies), Lava Lamp, Bomb Rug, Fish Tank, Arcade Machine, Big Plant, Bookshelf.
The house has an open front so you can see in from the islands. **Your pets** (up to 6) play in the yard.
With the bed, bedtime shows 🛏️ and you wake up "well rested" with bonus coins.

**Mayor's phone missions:** every minute or two the phone rings (📞) with a timed job, shown in an orange HUD bar and a
yellow light beam: find the missing cat on a rooftop (120 s), deliver the pizza across the city (60 s, take your car!),
or catch the runaway balloon (90 s). Finish it for coins, XP, fireworks and cheering.

**City Hall's secret office:** walk into City Hall's front door to visit the Mayor's office (desk, portrait, flags).
Touch the glowing red book on the bookshelf to open the **secret vault** full of gold; the treasure chest gives a big
one-time reward. The green door takes you back outside.

**New bombs:** 🧲 **Magnet bomb** (level 9+) pulls everyone nearby toward it while its fuse burns. 🎈 **Balloon bomb**
(level 6+) floats down slowly on a balloon, drifting around, and pops when it lands.

**The Bomb King's Castle:** every 25th level is a showdown at the castle, a floating fortress with stone walls, towers and
banners under a purple night sky. The boss is always the Bomb King, twice as tough.

**Game modes** (menu → Game modes):
- 🏷️ **Tag** (with your bacon-hair buddies): one player gets the bomb (14–20 s fuse that doesn't reset). Pass it by touching
  someone. Whoever holds it when it blows is out; a new round starts. Last one standing wins.
- ⏱️ **Survival:** the bombs never stop and keep coming faster. Your time and best time are shown.

**Build Zone** (a checkered plot on the city land): stand in it to get Place / Remove / Color buttons (keys B / N / C).
Stack up to 10 blocks high, 300 blocks, 8 colors, to make your own parkour course. Blocks are saved and solid.

**Subway** 🚇: three entrances on the city sidewalk lead down to the Boomtopia Metro station. The train comes every
~16 s; stand inside it when it leaves to ride to the next stop (another entrance). The green door is the exit.

**Underwater world** 🤿: buy the **Diving suit** (600, in My House shop section) and you can swim instead of splashing:
hold Jump to swim up, jump near the surface to leap out. Explore the sunken city on the seabed: ruins, a statue of the
first Mayor, seaweed, coral, fish and 4 treasure chests. Underwater the view turns deep blue.

**Snowy Mountain** 🏔️: a big snowy mountain beyond the city. Ride the **ski lift** from the station on the city land to
the summit, then hop on the **sled** for a zig-zag run all the way back down.

**Small fun things**
- 🎉 **Dance party** (button or L): everyone dances (you, buddies, the crowd, the Mayor), disco lights and a beat.
- 📸 **Photo mode** (button or O): hides the buttons (pauses single player); Snap! shows the photo with a Save button.
- 🎁 **Mystery boxes** float down on parachutes during waves: coins, a power-up, a new pet, or even a locked skin!

## Skins (18 to unlock)
Whole new looks, unlocked by playing (not bought). The Shop's **Skins** section shows each one with a 🔒, its challenge
and a progress bar; unlocked skins have a Wear button ("Classic" = your normal shop look). Unlocking one pops up
"New skin unlocked!". Other players see your skin in multiplayer.
- Ninja (survive 20 waves) · Firefighter (rescue 50 people) · Astronaut (blast off 3 times) · Robot (smash 5 robots)
- Pirate (beat 10 levels) · Lava Knight (beat 5 bosses) · Ice Prince (pass 100 bombs) · Basketball Star (score 5 bomb baskets)
- Racer (finish 3 rooftop races) · Zombie (get a black face 25 times) · Mayor Jr. (rescue 300 people) · Golden Hero (XP level 25)
- Rainbow (pick up 1,000 coins) · Dino (own 10 pets) · Superhero (rescue 1,000 people) · Bomb Kid (pop 100 bombs with RPGs)
- Ghost (survive 200 waves) · Savior of Boomtopia (rescue all 10,000 people)

## Fun park and city life
**Rides**
- **Ferris wheel** (on the city land): 8 colorful cabins with lights. Walk into the bottom cabin and ride all the way around.
- **Rocket launch pad:** stand on the glowing pad: "3, 2, 1... BLAST OFF!" shoots you about 120 high ("SPACE!"), then a
  **parachute** opens and you float back down (you can steer).
- **Water slide:** climb the ledges up the blue-and-white tower, step to the front edge, and slide down a spiral tube.
  At the bottom you splash out over the sea and land on an island ("Wheee!").
- **Speedboats** (3) zoom round the sea with a white wake, and **hot-air balloons** (4) float above the edge of the city.
  Jump on to ride them.
- **Ziplines** (4) between tall skyscrapers: walk to the yellow pole on the roof and zoom down the cable to the other roof.

**Drive and fly** (press E / the action button near them; E again to get out)
- **Your own sports car** (with a spoiler) is parked on the sidewalk near the Mayor. Steer with the joystick / WASD, Shift
  for turbo, Jump to honk. You can drive anywhere on the city land; buildings stop you.
- **Your own green helicopter** is parked on City Hall's roof. Move to fly, hold Jump to go up, let go to come down.
  Jump out high up and a parachute opens.

**Rooftop races:** touch the green 🏁 ring on the sidewalk to start; fly/climb through 6 rings on rooftops in order
(the next one is gold, with a light beam). Your time and best time are shown; in multiplayer your time is posted in chat.

**Mayor and people**
- **Medals:** every 100 people rescued, the Mayor gives you a medal (coins + fireworks). Medals hang on a board by City Hall.
- **Rebuild Boomtopia:** every 25 people rescued, a family house (colored walls, roof, chimney, tree) is built in the city
  (up to 90). The menu's Mission card shows 🏅 medals and 🏠 houses.
- **Talking people:** rescued people stroll along the sidewalk and say funny things in speech bubbles when you walk past.

**Bacon-hair buddies help rescue:** when no bomb is near them, your buddies (Buddy, Zoe, Max…) run to the nearest
trapped-people bubble and pop it. Their rescues count for your mission (people, coins, XP, medals, houses); they say
"I saved 3!" and cheer. They also smash the Bomb King's robots. Bubbles they can't reach (across water) are left for you.

**Bomb fun**
- **Bomb storm** (sometimes, level 3+): the sky turns red, bombs come twice as fast for 30 seconds, coins are doubled.
- **The Bomb King's robots** (level 4+, single player): flying robots grab a trapped-people bubble and try to carry it
  away. Touch a robot (or blow it up) to smash it: the bubble drops back on an island. If it escapes, those people are lost.
- **Bomb basketball:** a hoop over the sea, about 10 steps from the island edge. Throw a bomb through it: "SWISH! +3",
  coins, XP and the crowd cheers.

**The world**
- **Day and night:** a whole day takes about 4 minutes. At night the sky darkens, stars come out, city windows light up and
  the helicopters' searchlights switch on.
- **Bedtime:** when night falls on a day map: "🌙 It's getting late...", then the screen fades to black ("Goodnight, hero!"
  with a lullaby, then "Zzz..."). The game pauses (single player). A phone rings: "🎩 Wake up, hero! The Mayor is calling you!",
  then it's morning ("Good morning, hero!"), you get a few coins and the Mayor says "Good morning, hero!" in his bubble.
  (Night maps like Space or Graveyard stay night and have no bedtime.)
- **Weather** changes every minute or so: sunny, rain, thunderstorms (lightning flashes and thunder) or snow.
- **Festival day (every Saturday):** party balloons rise over the city, fireworks, the crowd cheers, and **double XP**.

## Cool pack
- **Fancy graphics** (Settings; on for computers, off for phones): glow (bloom) on lava, crystals, fire and explosions, and real shadows.
- **Gradient sky** that fades from deep colour at the top to light at the horizon, on every map.
- **Bigger explosions**: a shockwave ring across the ground, smoke puffs that hang in the air, and a flash when one goes off near you.
- **Slow motion**: when a bomb explodes in someone's hands near you, time slows and the camera zooms in (single player only).
- **COMBO**: pass, pop or hit the boss again within 3 seconds for COMBO x2, x3… with bonus coins and XP.
- **Fireworks** for beating a level, beating a boss and levelling up.
- Dust puffs when landing or running fast, a sparkly trail when flying with a cape, and a camera that widens when you run or fly.

## Parkour on the buildings
- The city's skyscrapers are **solid**: land on the roofs, and the walls stop you.
- **Wall-jump:** touching a wall in the air, press Jump to kick up again. Tap it again and again to climb a building
  all the way to the roof. Hanging on a wall makes you **slide down slowly**.
- **Four parkour trails** lead from the islands out over the water to the city: colorful floating blocks (some are pink
  **trampolines** that launch you high), then zig-zag **ledges** up the wall to the roof. You can jump up through blocks from below.
- Each new roof you reach in a level: "Rooftop!" with its height, plus coins and XP.

## Bomb levels (Lv 1-10)
Every falling bomb has a level, shown by a colored band and a floating "Lv" badge (green Lv1 → lime → yellow → orange → red →
pink → purple → blue → cyan → gold Lv10; Lv8+ sparkle). Each level up: about 7% bigger, 8% wider blast, 12% more damage,
5% faster fall and a 3.5% shorter fuse. Higher game levels bring higher bomb levels (about Lv1 at level 1, Lv4-5 at
level 20, Lv9-10 at level 50; Survival ramps up with time), with a rare bomb 2 levels higher. The first time a new bomb
level appears: "⚠️ Level N bombs incoming!". Tougher bombs pay more coins and XP when you pass them or throw them away.
The 💣 **Bomb guide** (🎒 menu) shows all 10 levels (the ones you've met) and every kind of bomb.

## Big pack 4: soccer, karts, puzzles, dinos, sky city, pirates, quests and more
**New ways to play** (menu → Game modes)
- ⚽ **Bomb soccer:** 2 vs 2 in a stadium with a cheering crowd. Run into the giant bomb-ball to kick it; first to 3 goals
  wins. If nobody scores in 40 s the ball explodes and it's kick-off again.
- 🏎️ **Kart racing:** 3 laps of the city ring road against 3 karts. Drive through ? boxes for a 🚀 boost or a 🍌 banana
  (Jump to use). Finish 1st to win.
- 👑 **King of the hill:** stay in the middle of the map for the most time in 60 s while everyone bumps each other off.
- 🧩 **Puzzle tower** (🧩 kiosk on the sidewalk): 3 rooms: step on all the pressure plates, push the crate onto the gold
  square, then press the colored buttons in the order shown on the wall. Treasure at the top.

**Creatures and friends**
- 🦖 **Dinosaur island** (🦖 Dino boat kiosk): a jungle island with roaming dinos. Press E by the T-Rex to ride it; Jump to ROAR.
- ⚔️ **Pet battles** (🎒 menu): pick one of your pets and fight a wild pet: Attack, Super (strong but can miss) or Heal.
- 🤖 **Robot buddy builder** (🎒 menu): smashing Bomb King robots gives ⚙️ parts. 10 parts build a robot buddy (pick its
  head and color) that hovers beside you and zaps a falling bomb near you every 10 s.

**New places**
- 🧊 **Ice cave** (🧊 kiosk): slippery ice, icicles, an ice slide, an ice dragon shooting freezing ice balls, and 3 frozen
  treasure chests (stand next to the ice to melt it).
- ☁️ **Sky city:** a giant beanstalk grows out of the sea. Jump up its leaves to the cloud city 120 high: castle houses and
  a goose that gives you a golden egg.
- 🏴‍☠️ **Pirate ship:** moored at the dock. E to sail around the sea, Jump fires the cannon at floating barrels, and sail up
  to the 3 little treasure islands.
- 🌋 **Inside the volcano** (🌋 Lava elevator kiosk): jump across rock platforms (some moving) over the lava to the
  volcano's crystal heart. Falling in hurts and sends you back.

**Big goals** (🎒 menu: the 🎒 button in game, or "More fun" on the menu)
- 📜 **Quest log:** 5 chapters of 3 quests each (rescue people, ride a train, go to the moon, win a tournament, beat the
  castle…). Claim a reward for each chapter; finishing all 5 shows the story's ending ("Boomtopia is saved!").
- 🗺️ **Treasure maps:** 5 map pieces are hidden: on a tall rooftop, under the sea, on the moon, in the sky city and inside
  the volcano. With all 5, a red X appears on the farthest island: walk onto it for the giant treasure.
- 🏅 **Season pass:** all XP also fills the season pass: 50 free tiers of coins, robot parts, pet eggs and skins.
- 📚 **Collection book:** pets, skins, fish and treasures you've found.

**Fun extras**
- 🎸 **Music studio:** an 8-row × 16-step beat maker (drums, bass, notes) with a speed slider; "Use as game music" plays
  your song in the game.
- 🎣 **Fishing:** at the end of the dock, E to cast, wait for the bite, then E to reel in. 12 catches from sardines to a
  whale, a bomb fish or an old boot.
- 🌱 **Garden farm:** 6 plots by your house. Walk on an empty plot to plant; after 3 minutes (real time) it becomes a
  glowing magic plant that gives a power-up when you pick it.
- 📺 **Boomtopia TV:** the game saves a snapshot of your best moments (bosses beaten, levels won, big rescues, golden
  bombs, combos, the moon, treasures…). Watch them on the TV in your house or from the 🎒 menu.

## Big pack 3: modes, pets, worlds, city life, powers and makers
**New ways to play** (menu → Game modes)
- 🏆 **Tournament:** an 8-player bracket (you + 7 named players). Each match is 1-on-1 bomb tag; win the quarterfinal,
  semifinal and final to become CHAMPION and win a gold trophy (big coins + XP, confetti).
- 🧟 **Zombie night:** on night maps (and at Halloween), slow bomb-zombies walk toward you each wave and hurt on touch.
  Blow them up with bombs or RPGs for coins.
- 🙈 **Hide and seek:** 20 seconds to hide anywhere (islands, city, rooftops), then 60 seconds of seekers walking the
  islands and the city. If one gets close it chases you; caught = game over, last the 60 seconds = you win.
- 🎯 **Target practice:** a shooting range on the city land with 5 moving bullseye targets. Hit them with RPG rockets or
  thrown bombs (bombs now explode when they land on the city). BULLSEYE = +25.

**Pets and friends**
- 🐎 **Ride your pet** (M / 🐎 button): you sit on your pet (shown twice as big) and go 1.7× faster; flying pets let you
  fly like a cape.
- 🥚 **Pet eggs** appear on the islands now and then. Pick one up and it hatches after 60 s of play into a new pet
  (rarer pets are more likely).
- 🤝 **Trading** (multiplayer, 🤝 button): pick a friend in the game and send them a pet (it leaves your collection) or
  a skin you've unlocked; they get a gift message.

**New worlds**
- 🌕 **Moon base:** the rocket now flies you all the way to the moon: craters, a glass dome, a flag, Earth in the black
  sky and super low gravity. Stand on the blue pad for 2 s to fly home (with a parachute).
- 🌋 **Volcano island:** a huge volcano far behind the city erupts every 15–25 s, shooting lava bombs.
- 🏜️ **Desert pyramid:** a pyramid in the far desert. Take the 🐪 Desert bus kiosk on the sidewalk into its tunnel:
  dodge spike traps lit by torches to reach the golden statue and the pharaoh's treasure.
- 🎢 **Theme park** (city land): a roller coaster with a hill, a loop-de-loop and a cart; a bumper-car arena (walk in to
  get a car, crash into the others: WHAM!; E to get out); and a haunted house full of flickering light and ghosts (BOO!).

**City life**
- 🍕 **Your own shop** (a striped stall on the sidewalk): stand behind it and serve customers the 🍕 🍦 🥤 🍔 they ask for.
- 💼 **Jobs** (job board near the Mayor): 🚒 firefighter (spray the fire on a rooftop), 🚓 police (catch the running
  robber) or 📦 delivery (take the package to the marker).
- 🏫 **School** (kiosk on the sidewalk): a classroom with a teacher; a 5-question quiz (sums, times tables, counting
  emojis) for XP.
- 🎃 **Holidays** (Settings → Holiday: Auto/Halloween/Christmas/Easter/Off): Halloween pumpkins, bats and zombies;
  Christmas tree with a daily present, Santa hats and snow; Easter egg hunt (10 eggs).

**Super powers**
- ⚡ **Power shop** (Shop): Super Speed, Shrink Ray (half damage), Teleport, Invisibility (bombs don't aim at you,
  nobody passes to you), Ice Breath (freezes bombs). Equip one; G / ⚡ to use, with a cooldown.
- 🌀 **Ultimate move:** a meter fills as you play (faster when you pass bombs and rescue people). When it's full,
  U / 🌀: a TORNADO blows away every bomb near you and a dome shield protects you for 8 seconds.

**Make it yours**
- 🎨 **Skin maker** (Shop): pick colors for shirt, pants, skin, hair and stripe, plus a hat, and wear "My Skin".
- 🏠 **Bigger house** (Shop → My House): Second Floor (stairs, bedroom, taller house), Swimming Pool and Flower Garden.
- 🗺️ **Map maker** (menu → Maps): paint a 22×22 grid of land, center, bridges and water, then play "My Map". Copy a map
  code to share with friends, or load one they send you.

## The 10,000x cooler pack
- **Cinematic intro:** every level starts with the camera swooping down from the sky around you.
- **Comic-book explosions:** BOOM! KAPOW! BLAM! WHAM! words pop out of explosions near you.
- **Speed lines** stream around the screen when you go really fast (turbo, car, sled, slide, zipline, rocket).
- **Hero titles and auras** by XP level: 💎 Hero (10+, blue sparkles), 🌟 Legend (25+, gold), 🌈 Mythic (50+, rainbow).
- **Level up:** a pillar of light and a ring of gold sparks.
- **Combo announcer:** NICE! (3) · AWESOME! (5) · UNSTOPPABLE! (8) · LEGENDARY! (12), with flashing colors.
- **Wave start** drum hit and golden screen pulse; **boss arrival**: striped ⚠️ WARNING ⚠️ banner, lightning and shaking.
- **Victory:** slow motion, fireworks and confetti cannons from both sides of the screen.
- **Golden bombs** (rare, shiny): when they blow they make a shower of coins.
- **Night skies:** shooting stars, and glowing aurora ribbons on night maps. **A rainbow** appears after the rain.

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
- One file: `bomb3d/index.html`, using Three.js (r128 from cdnjs) plus its glow (bloom) add-ons (from jsDelivr). No build step.
- Sounds are made in code (Web Audio), so there are no asset files.
