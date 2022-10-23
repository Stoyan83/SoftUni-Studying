const{ expect } = require('chai')
const { mathEnforcer } = require('./mathEnforcer')


describe("Math Enforcer", () => {
  describe('Add Five', () => {
    it ("should return undefined if not number", () => {
      expect(mathEnforcer.addFive('string')).to.eql(undefined)
    })

    it ("should return unum plus five", () => {
      expect(mathEnforcer.addFive(5)).to.eql(10)
    })

    it ("should return unum plus five", () => {
      expect(mathEnforcer.addFive(-5)).to.eql(0)
    })

    it ("should return unum plus five", () => {
      expect(mathEnforcer.addFive(-5.5)).to.be.closeTo(0,5, 0.01)
    })

    it ("should return unum plus five", () => {
      expect(mathEnforcer.addFive(5.5)).to.be.closeTo(10.5, 0.01)
    })

    describe('Subtract Ten', () => {
      it ("should return undefined if not number", () => {
        expect(mathEnforcer.subtractTen('string')).to.eql(undefined)
      })

      it ("should return num minus 10", () => {
        expect(mathEnforcer.subtractTen(11)).to.eql(1)
      })

      it ("should return num minus 10", () => {
        expect(mathEnforcer.subtractTen(-10)).to.eql(-20)
      })

      it ("should return num minus 10", () => {
        expect(mathEnforcer.subtractTen(-5.5)).to.be.closeTo(-15.5, 0.01)
      })

      it ("should return num minus 10", () => {
        expect(mathEnforcer.subtractTen(15.5)).to.be.closeTo(5.5, 0.1)
      })
    })

    describe('Subtract Ten', () => {
      it ("should return undefined if not number", () => {
        expect(mathEnforcer.sum('string', 10)).to.eql(undefined)
      })

      it ("should return undefined if not number", () => {
        expect(mathEnforcer.sum(20, 'string')).to.eql(undefined)
      })

      it ("should return undefined if not number", () => {
        expect(mathEnforcer.sum('string', 'string')).to.eql(undefined)
      })

      it ("should return undefined if not number", () => {
        expect(mathEnforcer.sum('string', 'string')).to.eql(undefined)
      })

      it ("should sum two number", () => {
        expect(mathEnforcer.sum(20, 10)).to.eql(30)
      })

      it ("should sum two number", () => {
        expect(mathEnforcer.sum(20, -10)).to.eql(10)
      })

      it ("should sum two number", () => {
        expect(mathEnforcer.sum(-10, -10)).to.eql(-20)
      })

      it ("should sum two number", () => {
        expect(mathEnforcer.sum(-10.5, -10.5)).to.be.closeTo(-21, 0.01)
      })

      it ("should sum two number", () => {
        expect(mathEnforcer.sum(10.5, 10.5)).to.be.closeTo(21, 0.01)
      })

    })


  })
})