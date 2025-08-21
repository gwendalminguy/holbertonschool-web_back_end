/* eslint no-underscore-dangle: 0 */
import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    if (typeof range !== 'string') {
      console.log(typeof range);
      throw TypeError('Range must be a string');
    }

	this._range = range;
  }

  cloneCar() {
	return new Car(this._brand, this._motor, this._color);
  }
}
