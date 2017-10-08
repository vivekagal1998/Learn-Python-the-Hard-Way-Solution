$def with (title, name, *numbers)
<html>
<head>
<title>$title</title>
</head>
<body>
<p>You are visiting page <b>$name</b>.</p>
<p>Find the answer to all questions below:
$for number in numbers:
    <p>$number</p>
</body>
</html>
