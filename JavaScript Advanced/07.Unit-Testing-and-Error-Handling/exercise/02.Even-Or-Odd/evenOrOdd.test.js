const{ expect } = require('chai')
const { isOddOrEven } = require('./evenOrOdd')


describe ('is od or even', () => {
  it ('should be undefined if number', () => {
    expect(isOddOrEven(10)).to.eql(undefined)
  })

  it ('should be undefined if arr', () => {
    expect(isOddOrEven([1,2,3])).to.eql(undefined)
  })

  it ('should be undefined if object', () => {
    expect(isOddOrEven({1:2, 2:2})).to.eql(undefined)
  })

  it ('should return odd', () => {
    expect(isOddOrEven('abc')).to.eql('odd')
  })

  it ('should return even', () => {
    expect(isOddOrEven('abcd')).to.eql('even')
  })
})