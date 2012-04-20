<result>
	<answer> { (: Which movies have the genre “special”? :)
		let $doc := doc("videos.xml")/result
		for $v in $doc/videos/video
		where data($v/genre) = "special"
		return $v/title
	}
	</answer>
	<answer> { (: Which director has directed at least two movies, and which movies has he directed? :)
		let $doc := doc("videos.xml")/result
		for $d in $doc/videos/video
		where 2 <= sum(for $v in $doc/videos/video
			 where data($d/director) = data($v/director)
			 return 1)
		return ($d/director, $d/title)
	}
	</answer>
	<answer> {(: Which are the top ten recommended movies? :)
		let $doc := doc("videos.xml")/result
		return subsequence(reverse(
			for $v in $doc/videos/video
			order by $v/user_rating
			return $v/title), 1, 10)
	}
	</answer>
	<answer> {(: Which actors have starred in the most movies? :)
		let $doc := doc("videos.xml")/result,
			$all := for $a in $doc/actors/actor
					return <a> { (
				  			$a, 
				  			<o> { 
				  				sum(
				  				for $v in $doc/videos/video
				  				where some $o in $v/actorRef satisfies data($o) = $a/@id
				  				return 1) }
				  			</o>
				  			) }
				  		</a>
		for $a in $all
		where max($all/o) = $a/o
		return $a/actor

	}
	</answer>
	<answer> {(: Which is one of the highest rating movie starring both Brad Pitt and Morgan Freeman? :) 
		let $doc := doc("videos.xml")/result,
			$mid := for $a in $doc/actors/actor
					where data($a) = "Freeman, Morgan"
					return $a/@id,
			$bid := for $a in $doc/actors/actor
					where data($a) = "Pitt, Brad"
					return $a/@id
		for $v in $doc/videos/video
		where (some $a in $v/actorRef satisfies data($a) = $mid) and (some $a in $v/actorRef satisfies data($a) = $bid)
		return $v/title
	}
	</answer>
	<answer> {(: Which actors have starred in a PG-13 movie between 1997 and 2006 (including 1997 and 2006)? :)
		let $doc := doc("videos.xml")/result,
			$all := for $v in $doc/videos/video
					where data($v/rating) = "PG-13" and 1997 <= data($v/year) and data($v/year) <= 2006
					return $v
		for $a in $doc/actors/actor
		where some $id in $all/actorRef satisfies $a/@id = data($id)
		return $a
	}
	</answer>
	<answer> {(: Who have starred in the most distinct types of genre? :)
		let $doc := doc("videos.xml")/result,
			$all := for $a in $doc/actors/actor
					return 	<a> { (
					  			$a, 
					  			<o> { 
					  				count(distinct-values(
					  				for $v in $doc/videos/video
					  				where some $o in $v/actorRef satisfies data($o) = $a/@id
					  				return data($v/genre))) }
					  			</o>
					  			) }
				  			</a>
		for $a in $all
		where max($all/o) = $a/o
		return $a/actor
	}
	</answer>
	<answer> {(: Which director have the highest sum of user ratings? :)
		let $doc := doc("videos.xml")/result,
			$all := for $d in distinct-values($doc/videos/video/director)
					return 	<d>
								<director>
								{($d)}
								</director>
								<o>{(sum(
									for $v in $doc/videos/video
									where $d = $v/director
									return data($v/user_rating)))}
								</o>
							</d>
							
		for $d in $all
		where max($all/o) = $d/o
		return $d/director
	}
	</answer>
	<answer> {(: Which movie should you recommend to a customer if they want to see a horror movie and do not have a laserdisk? :)
		let $doc := doc("videos.xml")/result
		return subsequence(reverse(
			for $v in $doc/videos/video
			where data($v/genre) = "horror" and ($v/vhs_stock > 0 or $v/beta_stock > 0 or $v/dvd_stock > 0)
			order by $v/user_rating
			return $v/title),
		1,1)
	}
	</answer>
	<answer> {(: Sort the movies after genre and user rating. :)
		let $doc := doc("videos.xml")/result
		for $g in $doc/video_template/genre/choice
		let $vs := 	for $v in $doc/videos/video
					where data($g) = data($v/genre)
					order by $v/user_rating
					return $v/title
		order by $g
		return 	<genre genre="{data($g)}">{
				$vs}
				</genre>
	}
	</answer>
</result>
