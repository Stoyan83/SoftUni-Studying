const{ expect } = require('chai')
const { isSymmetric } = require('./symettry')


describe("Check Symetry", () => {
  it('works with symmtric arr', () => {
    expect(isSymmetric([2,3,3,2])).to.be.true;
  })

  it('works with symmtric arr with odd length', () => {
    expect(isSymmetric([2, 3, 2])).to.be.true;
  })

  it('returns false for non symmetric arr', () => {
    expect(isSymmetric([2,4,3,2])).to.be.false;
    expect(isSymmetric([1,2,3])).to.be.false;
  })

  it('returns false for non arr obj', () => {
    expect(isSymmetric({1: 2})).to.be.false;
  })

  it('returns false not equal tyepes', () => {
    expect(isSymmetric([2,3,3,'2'])).to.be.false;
  })
})