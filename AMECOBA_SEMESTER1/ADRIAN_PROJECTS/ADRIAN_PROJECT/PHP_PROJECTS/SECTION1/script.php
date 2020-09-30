<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>HTML内にPHPのプログラムを組み込む</title>
</head>
<body>
<h1><?php echo "PHPで見出しを表示"; ?></h1>
<?php
$str = "変数も表示できます！";
echo "<p>{$str}</p>";
?>
</body>
</html>