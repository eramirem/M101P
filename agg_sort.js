use agg
db.zips.aggregate([
	{$match:
		{"state":'NY'}},
	{$group:
		{_id:"$city", "population":{$sum:"$pop"}}}, 
	{$project:
		{_id:0,city:"$_id", population:"$population"}},
	{$sort:
		{population: -1}
	}

])
