use agg;
db.grades.aggregate([{$unwind:"$scores"},{$match:{"scores.type":{$in:['homework','exam']}}},{$group:{_id:{student_id:"$student_id", class:"$class_id"}, average:{$avg:"$scores.score"}}},{$group:{_id:"$_id.class", average:{$avg:"$average"}}},{$sort:{average:-1}},{$limit:1}])
