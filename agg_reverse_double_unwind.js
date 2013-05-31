use test;
db.inventory.aggregate([
	{$unwind:"$sizes"},
	{$unwind:"$colors"},
	{$group:{
		_id:{name:"$name", size:"$sizes"},
		colors:{$push:"$colors"}
	}},
	{$group:{
		_id:{name:"$_id.name", colors:"$colors"},
		sizes:{$push:"$_id.size"}
	}},
	{$project:{
		_id: 0,
		name: "$_id.name",
		sizes: 1,
		colors: "$_id.colors"
	}}
			
])
