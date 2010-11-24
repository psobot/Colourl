<div style="font-family: zapfino, cursive; margin: 0 auto; font-size: 6em; width: 600px; text-align: center;">
<?php
	$output = "";
	$out = exec( "wc output.csv" , $output );
	$output = explode( " ", $out );
	echo $output[1];
?>
