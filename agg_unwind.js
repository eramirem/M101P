use blog;
db.posts.aggregate([
	{$unwind:"$tags"},
	{$group:{_id:"$tags", count:{$sum:1}}},
	{$sort:{count:-1}},
	{$limit:10},
	{$project:{_id:0, tags:"$_id", count:1}}
])
