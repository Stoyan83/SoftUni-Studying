const{ expect } = require('chai')
const { lookupChar } = require('./lookupChar')

describe ('Char Look up', () => {
  it('should return undefined if not string', () => {
    expect(lookupChar(100, 2)).to.eql(undefined)
  })


  it('should return undefined if not string', () => {
    expect(lookupChar('abc', 0.1)).to.eql(undefined)
  })


  it('should return undefined if index not an integer', () => {
    expect(lookupChar('abc', 'a')).to.eql(undefined)
  })

  it('should return incorect index if index >= string length', () => {
    expect(lookupChar('abc', 3)).to.eql('Incorrect index')
  })

  it('should return incorect index < 0', () => {
    expect(lookupChar('abc', -2)).to.eql('Incorrect index')
  })

  it('showing the right char at index', () => {
    expect(lookupChar('abc', 1)).to.eql('b')
  })

})