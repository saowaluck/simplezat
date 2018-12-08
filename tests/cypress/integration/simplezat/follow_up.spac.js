
context('Rating', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8000')
  })


  it('should have 3 rating', () => {
    cy.contains('How do we do')
    cy.get('img').should('have.attr', 'alt', 'Positive')
    cy.get('img').should('have.attr', 'alt', 'Neutral')
    cy.get('img').should('have.attr', 'alt', 'Negative')

    cy.get('img["Positive"]').click()
    cy.wait(1000)

    cy.contains('Any comment?')
    cy.get('inputp[name=comment"]').type('You are doing great!')
    cy.get('button').click()
    cy.wait(1000)

    cy.contains('Thank you')
  })
})
