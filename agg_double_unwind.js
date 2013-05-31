use test;
db.inventory.aggregate([
	{$unwind:"$sizes"},
	{$unwind:"$colors"},
	{$group:{
		_id:{sizes:"$sizes", colors:"$colors"},
		count:{$sum:1}
	}}
])
