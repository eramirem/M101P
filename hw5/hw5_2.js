use agg;
db.zips.aggregate([{$match:{state:{$in:['CA','NY']}}}, {$group:{_id:{state:"$state", city:"$city"}, population:{$sum:"$pop"}}},{$match:{population:{$gte:25000}}}, {$group:{_id:null, avg:{$avg:"$population"}}}])
