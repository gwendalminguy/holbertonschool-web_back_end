/* eslint no-underscore-dangle: 0 */
export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw TypeError('SQFT must be a number');
    }

    this._sqft = sqft;
  }

  // SQFT
  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    if (typeof value !== 'number') {
      throw TypeError('SQFT must be a number');
    }
    this._sqft = value;
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
