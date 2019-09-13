'''archive'''


'''
def hilbert_transform_inst_trendline(data):
    """Hilbert Transform - Instantaneous Trendline"""
    try:
        logger.info(
            'Calculating Hilbert Transform - Instantaneous Trendline...')
        htit_data = talib.HT_TRENDLINE(data)
        return htit_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def hilbert_transform_dom_cyc_per(data):
    """Hilbert Transform - Dominant Cycle Period"""
    try:
        logger.info('Calculating Hilbert Transform - Dominant Cycle Period')
        htdcp_data = talib.HT_DCPERIOD(data)
        return htdcp_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def hilbert_transform_dom_cyc_phase(data):
    """Hilbert Transform - Dominant Cycle Phase"""
    try:
        logger.info('Calculating Hilbert Transform - Dominant Cycle Phase')
        htdcp_data = talib.HT_DCPHASE(data)
        return htdcp_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def hilbert_transform_phasor_components(close):
    """Hilbert Transform - Phasor Components"""
    try:
        logger.info("Calculating Hilbert Transform - Phasor Components...")
        inphase_data, quadrature_data = talib.HT_PHASOR(close)
        df = pd.DataFrame()
        df['inphase'] = inphase_data
        df['quadrature'] = quadrature_data
        return df
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def hilbert_transform_sine_wave(data):
    """Hilbert Transform - Sine Wave"""
    try:
        logger.info("Calculating Hilbert Transform - Sine Wave...")
        sine_data, leadsine_data = talib.HT_SINE(data)
        df = pd.DataFrame()
        df['sine'] = sine_data
        df['leadsine'] = leadsine_data
        return df
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def hilbert_transform_trend_vs_cycle_mode(data):
    """Hilbert Transform - Trend vs cycle mode"""
    try:
        logger.info("Calculating Hilbert Transform - Trend vs cycle mode...")
        httc_data = talib.HT_TRENDMODE(data)
        return httc_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def parabolic_sar(high, low, af_step=.02, af_max=.2):
    """Parabolic SAR"""
    try:
        logger.info('Calculating Parabolic SAR...')
        check_inputs_length(high, low)
        ps_data = talib.SAR(high, low, acceleration, maximum)
        return ps_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception

def linear_regression(data, period):
    """Linear Regression"""
    try:
        logger.info(
            'Calculating Linear Regression for period = {}'.format(period))
        check_period_type(period)
        
        lr_data = talib.LINEARREG(data, timeperiod=period)
        return lr_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def linear_regression_angle(data, period):
    """Linear Regression Angle"""
    try:
        logger.info(
            'Calculating Linear Regression Angle for period = {}'.format(
                period))
        check_period_type(period)
        
        lra_data = talib.LINEARREG_ANGLE(data, timeperiod=period)
        return lra_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def linear_regression_intercept(data, period):
    """Linear Regression Intercept"""
    try:
        logger.info(
            'Calculating Linear Regression Intercept for period = {}'.format(
                period))
        check_period_type(period)
        
        lri_data = talib.LINEARREG_INTERCEPT(data, timeperiod=period)
        return lri_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def linear_regression_slope(data, period):
    """Linear Regression Slope"""
    try:
        logger.info(
            'Calculating Linear Regression Slope for period = {}'.format(
                period))
        check_period_type(period)
        
        lrs_data = talib.LINEARREG_SLOPE(data, timeperiod=period)
        return lrs_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception

def midpoint_over_period(data, period):
    """Midpoint over period"""
    try:
        logger.info(
            'Calculating Midpoint Over Period for period = {}'.format(period))
        check_period_type(period)
        
        mop = talib.MIDPOINT(data, timeperiod=period)
        return mop
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def midpoint_price_over_period(high, low, period):
    """Midpoint price over period"""
    try:
        logger.info(
            'Calculating Midpoint Price Over Period for period = {}'.format(
                period))
        check_period_type(period)
            
        check_inputs_length(high, low)
        mpop = talib.MIDPRICE(high, low, timeperiod=period)
        return mpop
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception

def absolute_price_oscillator(data, short_period, long_period, matype=0):
    """Absolute Price Oscillator"""
    try:
        logger.info(
            'Calculating Absolute Price Oscillator for Short period = {} and Long period = {}'
            .format(short_period, long_period))
        for period in (short_period, long_period):
            check_period_type(period)
            
        apo_data = talib.APO(data, short_period, long_period, matype=matype)
        return apo_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception

def normalized_average_true_range(high, low, close, period):
    try:
        """Normalized Average True Range"""
        logger.info(
            'Calculating Normalized Average True Range for period = {}'.format(
                period))
        check_period_type(period)
        check_inputs_length(high, low, close)
        natr_data = talib.NATR(high, low, close, timeperiod=period)
        return natr_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception

def true_range(high, low, close):
    """True Range"""
    try:
        logger.info('Calculating True Range...')
        check_inputs_length(high, low, close)

    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception

def balance_of_power(open, high, low, close):
    """Balance of Power"""
    try:
        logger.info("Calculating balance of Power...")
        check_inputs_length(open, high, low, close)
        bop_data = talib.BOP(open, high, low, close)
        return bop_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def correlation_coefficient(high, low, period):
    """Correlation Coefficient"""
    try:
        logger.info(
            "Calculating Correlation Coefficient for period = {}".format(
                period))
        check_period_type(period)
        check_inputs_length(high, low)
        cor_co_data = np.corrcoef(high,low)#talib.CORREL(high, low, timeperiod=period)
        return cor_co_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception

def chaikin_oscillator(high,
                       low,
                       close,
                       volume,
                       short_period=3,
                       long_period=10):
    """Chaiking oscillator"""
    try:
        logger.info(
            'Calculating Chaikin Oscillator for short period = {} and long period = {}'
            .format(short_period, long_period))
        check_inputs_length(high, low, close, volume)
        for period in (short_period, long_period):
            check_period_type(period)
        df = pd.DataFrame()
        df['chaikin_ad_line'] = talib.AD(high, low, close, volume)
        df['chaikin_oscillator'] = talib.ADOSC(high,
                                               low,
                                               close,
                                               volume,
                                               fastperiod=short_period,
                                               slowperiod=long_period)
        return df
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception

def positive_directional_movement(high, low):
    """
    Positive Directional Movement
    """
    try:
        up_moves = [high[idx] - high[idx-1] for idx in range(1, len(high))]
        down_moves = [low[idx] - low[idx-1] for idx in range(1, len(low))]

        pdm = []
        for idx in range(0, len(up_moves)):
            if up_moves[idx] > down_moves[idx] and up_moves[idx] > 0:
                pdm.append(up_moves[idx])
            else:
                pdm.append(0)

        return pdm
    except Exception as exception:
        raise exception

def negative_directional_movement(high, low):
    """
    Negative Directional Movement 
    """
    up_moves = [high[idx] - high[idx-1] for idx in range(1, len(high))]
    down_moves = [low[idx] - low[idx-1] for idx in range(1, len(low))]

    ndm = []
    for idx in range(0, len(down_moves)):
        if down_moves[idx] > up_moves[idx] and down_moves[idx] > 0:
            ndm.append(down_moves[idx])
        else:
            ndm.append(0)

    return ndm

def positive_directional_index(high, low, close, period, ignore_log=False):
    '''positive directional index'''  
    try:
        if ignore_log!=True:
            logger.info("Calculating Positive Directional Index for period = {}".format(period))
        pdi = (100 *
           smma(positive_directional_movement(high, low), period) /
           atr(close, period)
           )
        return pdi
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception
     

def negative_directional_index(high, low, close, period,ignore_log=False):
    try:
        '''negative directional index'''
        if ignore_log!=True:
            logger.info("Calculating Negative Directional Index for period = {}".format(period))
        ndi = (100 *
           smma(negative_directional_movement(high, low), period) /
           atr(close, period)
           )
        return ndi
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def average_directional_index(high, low, close, period):
    """Average Directional Index"""
    try:
        logger.info(
            'Calculating Average Directional Index for period = {}'.
            format(period))
        check_period_type(period)
        check_inputs_length(high, low, close)

        avg_di = (abs((positive_directional_index(close, high, low, period,ignore_log=True) - negative_directional_index(close, high, low, period,ignore_log=True)) /
              (positive_directional_index(
                close, high, low, period,ignore_log=True) +
               negative_directional_index(
                close, high, low, period,ignore_log=True)))
              )
        adx = 100 * smma(avg_di, period)
        return adx
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def directional_movement_index(high, low, close, period):
    """Directional Movement Index"""
    try:
        logger.info(
            "Calculating Directional Movement Index for period = {}".format(
                period))
        check_period_type(period)
        check_inputs_length(high, low, close)
        dmo_data = talib.DX(high, low, close, timeperiod=period)
        return dmo_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def minus_directional_indicator(high, low, close, period):
    """Minus Directional Indicator"""
    try:
        logger.info(
            'Calculating Minus Directional Indicator for period = {}'.format(
                period))
        check_period_type(period)
        check_inputs_length(high, low, close)
        mdi_data = talib.MINUS_DI(high, low, close, timeperiod=period)
        return mdi_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def minus_directional_movement(high, low, close, period):
    """Minus Directional Movement"""
    try:
        logger.info(
            'Calculating Minus Directional Movement for period = {}'.format(
                period))
        check_period_type(period)
        check_inputs_length(high, low, close)
        mdm_data = talib.MINUS_DM(high, low, timeperiod=period)
        return mdm_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception

def plus_directional_indicator(high, low, close, period):
    """Plus Directional Indicator"""
    try:
        logger.info(
            'Calcluating Plus Directional Indicator for period = {}'.format(
                period))
        check_period_type(period)
        check_inputs_length(high, low, close)
        pdi_data = talib.PLUS_DI(high, low, close, timeperiod=period)
        return pdi_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def plus_directional_movement(high, low, close, period):
    """Plus Directional Movement"""
    try:
        logger.info(
            'Calcluating Plus Directional Movement for period = {}'.format(
                period))
        check_period_type(period)
        check_inputs_length(high, low, close)
        pdm_data = talib.PLUS_DM(high, low, timeperiod=period)
        return pdm_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception

'''