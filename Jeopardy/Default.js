var xhr = new XHLHttpRequest()

xhr addEventListener('load', getCategories() {
	if(xhr.status == 200) {

		console.log(xhr.response)
	} else {
		console.log(xhr.statusText)
	}
})

xhr addEventListener('error', function() {
	console.log(Error('Network Error'))
})

xhr.open('GET', "https://jservice.io/api/categories?count=5&offset=10")
xhr.send()

var categories = document.getElementId("test");

function getCategories() {
	JSON.parse(xhr.response)
}

function getQuestion(id) {
	'jservice...'+id
}