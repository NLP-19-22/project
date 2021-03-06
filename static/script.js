(() => {
  const plagiarismCheckerForm = document.querySelector('#plagiarismCheckerForm')
  const sensitivitySlider = document.querySelector('#sensitivity')
  const sensitivityPercentage = document.querySelector('#sensitivityPercentage')
  const resultsContainer = document.querySelector('#resultsContainer')
  const resultsTableBody = document.querySelector('#resultsTableBody')
  const noResultsContainer = document.querySelector('#noResults')
  const loader = document.querySelector('#loader')
  
  const handleFormSubmission = event => {
    event.preventDefault()

    resultsContainer.style.display = 'none'
    loader.style.display = 'block'
    fetch('/api/search', {
      method: 'POST',
      body: new FormData(plagiarismCheckerForm),
    })
      .then(response => response.json())
      .then(generateResultsTable)
      .catch((error) => {
        console.error(error)
        alert('Whoops! Something went wrong while searching.')
        loader.style.display = 'none'
      })
  }

  const generateResultsTable = data => {
    const tableBodyContent = data.reduce((output, item) => {
      output += `<tr><td class="titleColumn"><a href=${item.link} target="_blank"><p>${item.title}</p></a></td>
                  <td class="scoreColumn">${(item.score * 10).toFixed(2)}%</td>
                  <td class="detailColumn"><a href="#detailModal" class="btn btn-primary" data-toggle="modal" data-url="${item.link}" data-result="${item.text}">
                                            View
                                          </a></td></tr>`
      return output
    }, '')

    resultsTableBody.innerHTML = tableBodyContent

    const sliderValue = sensitivitySlider.value
    showTableRowsAboveSpecifiedPercentage(sliderValue)
    loader.style.display = 'none'
    resultsContainer.style.display = 'block'
  }

  const handleSliderChange = event => {
    const sliderValue = event.target.value

    updateSliderDisplayValue(sliderValue)
    showTableRowsAboveSpecifiedPercentage(sliderValue)
  }

  const updateSliderDisplayValue = sliderValue => {
    sensitivityPercentage.textContent = sliderValue
  }

  const showTableRowsAboveSpecifiedPercentage = sliderValue => {
    const tableRowMatchScores = document.querySelectorAll('td.scoreColumn')

    tableRowMatchScores.forEach(
      scoreCell => showTableRowAboveSpecifiedPercentage(scoreCell, sliderValue)
    )

    const visibleTableRows = document.querySelectorAll('#resultsTableBody tr:not(.hidden)')

    if (visibleTableRows.length > 0) {
      noResultsContainer.classList.add('hidden')
    } else {
      noResultsContainer.classList.remove('hidden')
    }
  }

  const showTableRowAboveSpecifiedPercentage = (scoreCell, sliderValue) => {
    const score = Number(scoreCell.textContent.replace('%', ''))
    const tableRow = scoreCell.parentElement

    if (score > sliderValue) {
      tableRow.classList.remove('hidden')
    } else {
      tableRow.classList.add('hidden')
    }
  }

  plagiarismCheckerForm.addEventListener('submit', handleFormSubmission)
  sensitivitySlider.addEventListener('input', handleSliderChange)
})()
