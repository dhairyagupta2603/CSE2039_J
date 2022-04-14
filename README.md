# Kingdom of Circles
<p>
It is a orignal highscore based game taking inspiration from many classical games like pac-man, chess, spy mouse, etc. It is made using Pygame and the scores are stored in Firebase as the database.
</p>

### Board Design
<p>
The board is tiled green with black borders interpreted as grass tiles. This board is surrounded by grey colored walls which serve as a barrier so that the player does not go out of bounds. The same walls also act os obstacles for enemy so that the player can navigate through the board using an elemnt of startagy especially during later stages when the enemies match player movement and one miss-step can cause the player to be trapped. 
</p>
![board img](docs\board_img.png)

### Player
<p>
The Player character is charcaterized by a Blue circle which has a 8-direction movement controlled as follows: -
<ul>
	<li>W - moves player Up</li>
	<li>A - moves the player Left</li>
	<li>X - moves the plyer Down</li>
	<li>D - moves the player Right</li>
	<li>Q - moves the player in Upper-Left direction</li>
	<li>E - moves the player in Upper-Right direction</li>
	<li>C - moves the player in Lower-Right direction</li>
	<li>Z - moves the player in Lower-Left direction</li>
</ul>
</p>
<!-- Player image here with direction arrows if possible -->

### Enemies
<p>
**YELLOW ENEMY**<br>
These enemies can only move in the Top-Down-Left-Right directions one tile at a time on the board and are fairly easy to avoid if there is only one but the player can be easily trapped if multiple of these are on the board.
</p>
<!-- Yellow enemy image here with direction arrrows if possible -->

<p>
**VIOLET ENEMY**<br>
These enemies can only move in the diagonal directions one tile at a time on the board and are also fairly easy to avoid. Due to how they traverse, one Violet enemy can only travel to half of the board and depending on the spawn have a chance of getting stuck until upgraded. Even multiple of these are not much oof a threat to the player.
</p>
<!-- Violet enemy image here with direction arraows if possible -->


<p>
**RED ENEMY**<br>
These are the bosses of this game and even one is a major threat to the player as it can follow the player anyware and will almost always be only one step behind, ready to trap the player with one miss-step. Using the walls to your advantage is the only way to evade them. At max only 2 of these can be on the board at the same time but they are a force to be reconed with.
</p>
<!-- Red enemy image here with direction arraows if possible -->

### Enemy AI in action
<p>
The enemies irrespective of type interact ith each other after each player move to determine the best possible moves for each of them. If the player in in the center, they will tend to disperse themselves so that player is closer to reach for any one of them at a time, but if a player is in the corners, they will try to stick close together to mazimize the chance of trapping the player. This interaction is dependent on score and the number of enemies on the board.
</p>

### Future Work
<p>
Texturing and difficulty scaling
</p>
