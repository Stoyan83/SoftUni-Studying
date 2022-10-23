function solve() {
  canFight = function (hero) {
    hero.fight = function () {
      hero.stamina--;
      console.log(`${hero.name} slashes at the foe!`);
    };
  };
  canCast = function (hero) {
    hero.cast = function (spell) {
      hero.mana -= 1;
      console.log(`${hero.name} cast ${spell}`);
    };
  };

  const genHero = function (name) {
    return { name, health: 100 };
  };

  const mage = function (name) {
    let hero = genHero(name);
    hero.mana = 100;
    return Object.assign(hero, canCast(hero));
  };

  const fighter = function (name) {
    let hero = genHero(name);
    hero.stamina = 100;
    return Object.assign(hero, canFight(hero));
  };

  return { mage: mage, fighter: fighter };
}

let create = solve();
const scorcher = create.mage("Scorcher");
scorcher.cast("fireball");
scorcher.cast("thunder");
scorcher.cast("light");

const scorcher2 = create.fighter("Scorcher 2");
scorcher2.fight();

console.log(scorcher2.stamina);
console.log(scorcher.mana);
