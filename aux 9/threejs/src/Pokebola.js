/**
 Pokebola
 Clase pokebola.
 @author Pablo Pizarro R. @ppizarror.com
 @license MIT
 */
"use strict";

/**
 * Crea una Pokebola.
 *
 * @param {Point2D} pos_inicial - Posición inicial
 * @param {Point2D} velocidad_inicial - Velocidad inicial
 * @param {number} diametro_pokebola - Diámetro pokebola
 * @param {[number]} color_pokebola - Color pokebola
 * @param {number} alpha_elastico - Coeficiente de rebote
 * @param {number} plano - Posición del plano
 * @constructor
 */
function Pokebola(pos_inicial, velocidad_inicial, diametro_pokebola, color_pokebola,
                  alpha_elastico, plano) {

    // noinspection ES6ConvertVarToLetConst
    /**
     * Puntero al objeto
     */
    var self = this;

    /**
     * Guarda las variables
     */
    this._alpha = alpha_elastico;
    this._color = color_pokebola;
    this._dt = 1 / 60; // Incremento de tiempo
    this._g = 9.81; // "Gravedad"
    this._plano = plano;
    this._pos = pos_inicial;
    this._radio = diametro_pokebola / 2;
    this._vel = velocidad_inicial;

    /**
     * Crea el modelo en three.js
     */

}